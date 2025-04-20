import { childrenProps } from "../allInterface";
import useAuthContext from "../hooks/useAuthContext";
import { Navigate } from "react-router";

const PrivateRoute = ({ children }: childrenProps) => {
  const { user } = useAuthContext();
  if (user === null) return "Loading...";
  return user ? children : <Navigate to="/login"></Navigate>;
};

export default PrivateRoute;
