import { useEffect, useState } from "react";
import apiClint from "../services/api-clint";
type userLoginType = {
  email: string;
  password: string;
};
const useAuth = () => {
  const [user, setUser] = useState(null);
  const [errorMsg, setErrorMsg] = useState("");
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
      console.log("fetchUserProfile error", error);
    }
  };
  // Login User
  const loginUser = async (userData: userLoginType) => {
    setErrorMsg("");
    try {
      const response = await apiClint.post("/auth/jwt/create/", userData);
      setAuthTokens(response.data);
      localStorage.setItem("authTokens", JSON.stringify(response.data));

      // after Login
      await fetchUserProfile();
    } catch (error) {
      console.log(error);
      setErrorMsg(error.response.data?.detail);
    }
  };

  // register user
  const registerUser = async (userData) => {
    setErrorMsg("");
    try {
      await apiClint.post("/auth/users/", userData);
    } catch (error) {
      if (error.response && error.response.data) {
        const errMessage = Object.values(error.response.data).flat().join("\n");
        setErrorMsg(errMessage);
      } else {
        setErrorMsg("Registration Failed. Please Try Again");
      }
      // console.log(error);
    }
  };
  return { user, errorMsg, loginUser, registerUser };
};

export default useAuth;
