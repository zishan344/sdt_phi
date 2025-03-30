import { Route, Routes } from "react-router";
import MainLayout from "../layout/MainLayout";
import Home from "../pages/Home";
import Shop from "../pages/Shop";

const AppRoute = () => {
  return (
    <Routes>
      <Route element={<MainLayout />}>
        <Route path="/" element={<Home />} />
        <Route path="shop" element={<Shop />} />
      </Route>
    </Routes>
  );
};

export default AppRoute;
