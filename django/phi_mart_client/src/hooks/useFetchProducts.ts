import { useEffect, useState } from "react";
import apiClint from "../services/api-clint";

const useFetchProduct = (currentPage: number) => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [totalPage, setTotalPage] = useState(0);

  useEffect(() => {
    const fetchProducts = async () => {
      setLoading(true);
      try {
        const response = await apiClint.get(`/products?page=${currentPage}`);
        const data = await response.data;
        setProducts(data.results);
        setTotalPage(Math.ceil(data.count / data.results.length));
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    };
    fetchProducts();
  }, [currentPage]);

  return { products, loading, error, totalPage };
};

export default useFetchProduct;
