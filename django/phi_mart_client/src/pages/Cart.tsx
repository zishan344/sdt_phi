import { Suspense, useEffect, useState } from "react";
import useCartContext from "../hooks/useCartContext";
import CartItemList from "../components/Cart/CartItemList";
import CartSummary from "../components/Cart/CartSummary";

const Cart = () => {
  const {
    cart,
    createOrGetCart,
    updateCartItemQuantity,
    loading,
    deleteCartItems,
  } = useCartContext();
  const [localCart, setLocalCart] = useState(cart);

  useEffect(() => {
    createOrGetCart();
  }, [createOrGetCart]);
  useEffect(() => {
    setLocalCart(cart);
  }, [cart]);

  const handleUpdateQuantity = async (itemId, newQuantity) => {
    const prevLocalCartCopy = localCart;

    setLocalCart((prevLocalCart) => {
      const updateItems = prevLocalCart.items.map((item) =>
        item.id === itemId
          ? {
              ...item,
              quantity: newQuantity,
              total_price: item.product.price * newQuantity,
            }
          : item
      );
      return {
        ...prevLocalCart,
        items: updateItems,
        total_price: updateItems.reduce(
          (sum, item) => sum + item.total_price,
          0
        ),
      };
    });
    try {
      await updateCartItemQuantity(itemId, newQuantity);
    } catch (error) {
      console.log(error);
      setLocalCart(prevLocalCartCopy);
    }
  };

  const handleRemoveItem = async (itemId) => {
    setLocalCart((prevLocalCart) => {
      const updatedItems = prevLocalCart.items.filter(
        (item) => item.id != itemId
      );

      return {
        ...prevLocalCart,
        items: updatedItems,
        total_price: updatedItems.reduce(
          (sum, item) => sum + item.total_price,
          0
        ),
      };
    });

    try {
      await deleteCartItems(itemId);
    } catch (error) {
      console.log(error);
    }
  };

  if (loading) return <div>Loading...</div>;
  if (!localCart) return <p>No cart</p>;
  return (
    <div className="container mx-auto px-4 py-8">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div>
          <Suspense
            fallback={
              <div className="aspect-square bg-base-300 animate-pulse rounded-lg"></div>
            }>
            <CartItemList
              items={localCart.items}
              handleRemoveItem={handleRemoveItem}
              handleUpdateQuantity={handleUpdateQuantity}
            />
          </Suspense>
        </div>
        <div>
          <CartSummary
            itemCount={localCart.items.length}
            totalPrice={localCart.total_price}
          />
        </div>
      </div>
    </div>
  );
};

export default Cart;
