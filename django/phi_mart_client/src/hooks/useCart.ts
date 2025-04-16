import { useCallback, useState } from "react";
import apiClint from "../services/api-clint";
import authApiClient from "../services/auth-api-client";

const useCart = () => {
  const [authToken, setAuthToken] = useState(
    () => JSON.parse(localStorage.getItem("authTokens")).access
  );
  const [cart, setCart] = useState(null);
  const [cartId, setCartId] = useState(() => localStorage.getItem("cartId"));
  const [loading, setLoading] = useState(false);
  const createOrGetCart = useCallback(async () => {
    setLoading(true);
    try {
      console.log(authToken);
      const response = await authApiClient.post("/carts/");
      if (!cartId) {
        localStorage.setItem("cartId", response.data.id);
        setCartId(response.data.id);
      }
      setCart(response.data);
    } catch (error) {
      console.log(error);
    } finally {
      setLoading(false);
    }
  }, [authToken, cartId]);

  const AddCartItems = useCallback(
    async (product_id, quantity) => {
      if (!cartId) await createOrGetCart();
      console.log("Products", { product_id, quantity });
      try {
        const response = await authApiClient.post(`/carts/${cartId}/items/`, {
          product_id,
          quantity,
        });
        console.log(response);
        return response.data;
      } catch (error) {
        console.log(error);
      }
    },
    [cartId, createOrGetCart]
  );
  return { cart, createOrGetCart, AddCartItems };
};

export default useCart;
