import { Suspense, useEffect, useState } from "react";
import useCartContext from "../hooks/useCartContext";
import CartItemList from "../components/Cart/CartItemList";

const Cart = () => {
  const { cart, createOrGetCart, updateCartItemQuantity, loading } =
    useCartContext();
  const [localCart, setLocalCart] = useState(cart);

  useEffect(() => {
    createOrGetCart();
  }, [createOrGetCart]);
  useEffect(() => {
    setLocalCart(cart);
  }, [cart]);
  const handleRemoveItem = () => {};
  const handleUpdateQuantity = async (itemId, newQuantity) => {
    setLocalCart((prevLocalCart) => ({
      ...prevLocalCart,
      items: prevLocalCart.items.map((item) =>
        item.id === itemId ? { ...item, quantity: newQuantity } : item
      ),
    }));
    try {
      await updateCartItemQuantity(itemId, newQuantity);
    } catch (error) {
      console.log(error);
    }
  };
  if (loading) return <div>Loading...</div>;
  if (!localCart) return <p>No cart</p>;
  return (
    <div className="flex justify-between">
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
      <div></div>
    </div>
  );
};

export default Cart;
