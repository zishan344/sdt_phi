import { useEffect } from "react";
import useCartContext from "../hooks/useCartContext";

const Cart = () => {
  const { createCart } = useCartContext();
  useEffect(() => {
    createCart();
  }, []);
  return (
    <div>
      <h2>This is cart Page</h2>
    </div>
  );
};

export default Cart;
