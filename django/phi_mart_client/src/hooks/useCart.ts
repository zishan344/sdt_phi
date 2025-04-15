import { useState } from "react";
import apiClint from "../services/api-clint";
import authApiClient from "../services/auth-api-client";

const useCart = () => {
  const [authToken, setAuthToken] = useState(
    () => JSON.parse(localStorage.getItem("authTokens")).access
  );
  const [cart, setCart] = useState(null);
  const [cartId, setCartId] = useState(() => localStorage.getItem("cartId"));
  const createOrGetCart = async () => {
    console.log(authToken);
    try {
      const response = await authApiClient.post("/carts/");
      if (!cartId) {
        localStorage.setItem("cartId", response.data.id);
        setCart(response.data);
        setCartId(response.data.id);
      }
    } catch (error) {
      console.log(error);
    }
  };

  const AddCartItems = async (product_id, quantity) => {
    if (!cartId) await createOrGetCart();
    console.log("Products", { product_id, quantity });
    try {
      const response = await apiClint.post(
        `/carts/${cartId}/items/`,
        {
          product_id,
          quantity,
        },
        {
          headers: { Authorization: `JWT ${authToken}` },
        }
      );
      console.log(response);
      return response.data;
    } catch (error) {
      console.log(error);
    }
  };

  return { cart, createOrGetCart, AddCartItems };
};

export default useCart;
