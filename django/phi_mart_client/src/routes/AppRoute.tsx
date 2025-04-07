import { Route, Routes } from "react-router";
import MainLayout from "../layout/MainLayout";
import Home from "../pages/Home";
import Shop from "../pages/Shop";
import Login from "../pages/Login";

const AppRoute = () => {
  return (
    <Routes>
      <Route element={<MainLayout />}>
        <Route path="/" element={<Home />} />
        <Route path="shop" element={<Shop />} />
        <Route path="login" element={<Login />} />
      </Route>
    </Routes>
  );
};

export default AppRoute;
