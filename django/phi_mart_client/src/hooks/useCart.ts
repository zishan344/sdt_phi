import { useCallback, useState } from "react";
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
      setLoading(true);
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
      } finally {
        setLoading(false);
      }
    },
    [cartId, createOrGetCart]
  );

  const updateCartItemQuantity = useCallback(
    async (itemId, quantity) => {
      try {
        await authApiClient.patch(`/carts/${cartId}/items/${itemId}/`, {
          quantity,
        });
      } catch (error) {
        console.log("Error updating Cart items", error);
      }
    },
    [cartId]
  );

  const deleteCartItems = useCallback(
    async (itemId) => {
      try {
        await authApiClient.delete(`/carts/${cartId}/items/${itemId}/`);
      } catch (error) {
        console.log(error);
      }
    },
    [cartId]
  );
  return {
    cart,
    createOrGetCart,
    AddCartItems,
    updateCartItemQuantity,
    loading,
    deleteCartItems,
  };
};

export default useCart;
