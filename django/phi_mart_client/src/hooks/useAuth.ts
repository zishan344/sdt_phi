import React, { useState } from "react";
import apiClint from "../services/api-clint";

const useAuth = () => {
  const [user, setUser] = useState(null);
  const getToken = () => {
    const token = localStorage.getItem("authTokens");
    return token ? JSON.parse(token) : null;
  };

  const [authTokens, setAuthTokens] = useState(getToken());
  // Login User
  const loginUser = async (email: string, password: string) => {
    const response = await apiClint.post("/auth/jwt/create/", {
      email,
      password,
    });
    console.log(response.data);
  };
  return { user, loginUser };
};

export default useAuth;
