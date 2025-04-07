import { useContext } from "react";
import AuthContext from "../context/AuthContext";
import useAuthContext from "../hooks/useAuthContext";

const Login = () => {
  const { loginUser } = useAuthContext();
  return (
    <div>
      <h1>This is login page</h1>
      <button onClick={() => loginUser("zishanahmed344@gmail.com", "1234")}>
        Click to login
      </button>
    </div>
  );
};

export default Login;
