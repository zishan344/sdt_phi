import { Route, Routes } from "react-router";
import MainLayout from "../layout/MainLayout";
import Home from "../pages/Home";

const AppRoute = () => {
  return (
    <Routes>
      <Route element={<MainLayout />}>
        <Route path="/" element={<Home />} />
      </Route>
    </Routes>
  );
};

export default AppRoute;
