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
    setLocalCart((prevLocalCart) => ({
      ...prevLocalCart,
      items: prevLocalCart.items.map((item) =>
        item.id === itemId ? { ...item, quantity: newQuantity } : item
      ),
      total_price: prevLocalCart.items.reduce(
        (sum, item) => sum + item.total_price,
        0
      ),
    }));
    try {
      await updateCartItemQuantity(itemId, newQuantity);
    } catch (error) {
      console.log(error);
      setLocalCart(prevLocalCartCopy);
    }
  };
  const handleRemoveItem = async (itemId) => {
    setLocalCart((prevLocalCart) => ({
      ...prevLocalCart,
      items: prevLocalCart.items.filter((item) => item.id !== itemId),
    }));
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
