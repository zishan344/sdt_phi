import { useEffect, useState } from "react";
import apiClint from "../services/api-clint";
type userLoginType = {
  email: string;
  password: string;
};
const useAuth = () => {
  const [user, setUser] = useState(null);
  const getToken = () => {
    const token = localStorage.getItem("authTokens");
    return token ? JSON.parse(token) : null;
  };

  const [authTokens, setAuthTokens] = useState(getToken());
  useEffect(() => {
    if (authTokens) fetchUserProfile();
  }, [authTokens]);
  // Fetch user profile
  const fetchUserProfile = async () => {
    try {
      const response = await apiClint.get("/auth/users/me", {
        headers: { Authorization: `JWT ${authTokens?.access}` },
      });
      setUser(response.data);
    } catch (error) {
      console.log("Error fetching User", error);
    }
  };
  // Login User
  const loginUser = async (userData: userLoginType) => {
    try {
      const response = await apiClint.post("/auth/jwt/create/", userData);
      setAuthTokens(response.data);
      localStorage.setItem("authTokens", JSON.stringify(response.data));
    } catch (error) {
      console.log("Login Error", error?.data?.response);
    }
  };
  return { user, loginUser };
};

export default useAuth;
