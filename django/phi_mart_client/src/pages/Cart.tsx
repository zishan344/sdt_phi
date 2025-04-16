import { Suspense, useEffect } from "react";
import useCartContext from "../hooks/useCartContext";
import CartItemList from "../components/Cart/CartItemList";

const Cart = () => {
  const { cart, createOrGetCart, updateCartItemQuantity, loading } =
    useCartContext();

  useEffect(() => {
    createOrGetCart();
  }, [createOrGetCart]);
  const handleRemoveItem = () => {};
  const handleUpdateQuantity = async (itemId, newQuantity) => {
    try {
      await updateCartItemQuantity(itemId, newQuantity);
    } catch (error) {
      console.log(error);
    }
  };
  if (loading) return <div>Loading...</div>;
  if (!cart) return <p>No cart</p>;
  return (
    <div className="flex justify-between">
      <div>
        <Suspense
          fallback={
            <div className="aspect-square bg-base-300 animate-pulse rounded-lg"></div>
          }>
          <CartItemList
            items={cart.items}
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
