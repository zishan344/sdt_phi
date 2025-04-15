import { useEffect } from "react";
import useCartContext from "../hooks/useCartContext";

const Cart = () => {
  const { cart, createOrGetCart } = useCartContext();
  useEffect(() => {
    createOrGetCart();
  }, []);
  return (
    <div>
      <h2>This is cart Page</h2>
      <p>{JSON.stringify(cart)}</p>
    </div>
  );
};

export default Cart;
