import React from "react";
import useAuthContext from "../hooks/useAuthContext";
import { Navigate } from "react-router";

const PrivateRoute = ({ children }) => {
  const { user } = useAuthContext();
  if (user === null) return "Loading...";
  return user ? children : <Navigate to="/login"></Navigate>;
};

export default PrivateRoute;
