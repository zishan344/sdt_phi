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

  const handleAPIError = (
    error,
    defaultMessage = "Something Went Wrong! Try Again"
  ) => {
    console.log(error);
    if (error.response && error.response.data) {
      const errorMessage = Object.values(error.response.data).flat().join("\n");
      setErrorMsg(errorMsg);
      return { success: false, message: errorMessage };
    }
    setErrorMsg(defaultMessage);
    return {
      success: false,
      message: defaultMessage,
    };
  };

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

  // Update User Profile
  const updateUserProfile = async (data) => {
    setErrorMsg("");
    try {
      await apiClint.put("/auth/users/me", data, {
        headers: {
          Authorization: `JWT ${authTokens?.access}`,
        },
      });
    } catch (error) {
      return handleAPIError(error);
    }
  };

  //password change
  const changePassword = async (data) => {
    setErrorMsg("");
    try {
      await apiClint.post("/auth/users/set_password/", data, {
        headers: {
          Authorization: `JWT ${authTokens?.access}`,
        },
      });
    } catch (error) {
      return handleAPIError(error);
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
      return { success: true };
    } catch (error) {
      console.log(error);
      setErrorMsg(error.response.data?.detail);
      return { success: false };
    }
  };

  // register user
  const registerUser = async (userData) => {
    setErrorMsg("");
    try {
      await apiClint.post("/auth/users/", userData);
      return {
        success: true,
        message:
          "Registration successfull. Check your email to activate your account.",
      };
    } catch (error) {
      if (error.response && error.response.data) {
        const errorMessage = Object.values(error.response.data)
          .flat()
          .join("\n");
        setErrorMsg(errorMessage);
        return { success: false, message: errorMessage };
      }
      setErrorMsg("Registratation failed. Please try again");
      return {
        success: false,
        message: "Registratation failed. Please try again",
      };
    }
  };
  // logout user
  const logoutUser = () => {
    setAuthTokens(null);
    setUser(null);
    localStorage.removeItem("authTokens");
    localStorage.removeItem("cartId");
  };
  return {
    user,
    errorMsg,
    loginUser,
    registerUser,
    logoutUser,
    updateUserProfile,
    changePassword,
  };
};

export default useAuth;
