import { createContext } from "react";
import useAuth from "../hooks/useAuth";
import { childrenProps } from "../allInterface";

interface AuthContextType {
  email: string;
  password: string;
}
const AuthContext = createContext<AuthContextType | null>(null);
export const AuthProvider = ({ children }: childrenProps) => {
  const allContext = useAuth();
  return (
    <AuthContext.Provider value={allContext}>{children}</AuthContext.Provider>
  );
};

export default AuthContext;
