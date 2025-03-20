import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { CartItem } from "./type";

const CartApp = () => {
  const [cart, setCart] = useState([])
  const { register, handleSubmit } = useForm([]);
/*  const cart = [
    { id: 1, name: "laptop", price: 34000 },
    { id: 2, name: "mobile", price: 34000 },
    { id: 3, name: "tablet", price: 34000 }, 
  ];*/
  const addItem = (data: CartItem) => {
    const existingItem = cart.find(item=>item.name === data.name);
    if (existingItem) {
    setCart(
      cart.map(item=>item.name === data.name? {...item,quantity:item.quantity+1}:item
      )
    )
  };
  return <div></div>;
};

export default CartApp;
