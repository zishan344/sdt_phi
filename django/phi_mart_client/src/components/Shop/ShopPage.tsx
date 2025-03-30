import React, { useEffect, useState } from "react";
import apiClint from "../../services/api-clint";
import ProductList from "./ProductList";
import Pagination from "./Pagination";

const ShopPage = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [totalPage, setTotalPage] = useState(0);
  const [currentPage, setCurrentPage] = useState(1);
  useEffect(() => {
    fetchProduct();
  }, []);
  const fetchProduct = () => {
    setLoading(true);
    apiClint
      .get("/products")
      .then((res) => {
        setProducts(res.data.results);
        setTotalPage(Math.ceil(res.data.count / res.data.results.length));
      })
      .catch((err) => setError(err))
      .finally(() => setLoading(false));
  };
  return (
    <div>
      <ProductList products={products} loading={loading} error={error} />
      <Pagination
        totalPage={totalPage}
        currentPage={currentPage}
        handlePageChange={setCurrentPage}
      />
    </div>
  );
};

export default ShopPage;
