import { useState } from "react";
import apiClint from "../services/api-clint";

const useCart = () => {
  const [authToken, setAuthToken] = useState(
    () => JSON.parse(localStorage.getItem("authTokens")).access
  );
  const createCart = async () => {
    console.log(authToken);
    try {
      const response = await apiClint.post(
        "/carts/",
        {},
        {
          headers: { Authorization: `JWT ${authToken}` },
        }
      );
      console.log(response.data);
    } catch (error) {
      console.log(error);
    }
  };
  return { createCart };
};

export default useCart;
