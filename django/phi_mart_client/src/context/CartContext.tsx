import { createContext } from "react";
import useCart from "../hooks/useCart";
import { childrenProps } from "../allInterface";

const CartContext = createContext();

export const CartProvider = ({ children }: childrenProps) => {
  const allValue = useCart();
  return (
    <CartContext.Provider value={allValue}>{children}</CartContext.Provider>
  );
};

export default CartContext;
