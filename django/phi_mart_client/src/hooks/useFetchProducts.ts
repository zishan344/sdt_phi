import { useEffect, useState } from "react";

const useFetchProduct = (currentPage: number) => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [totalPage, setTotalPage] = useState(0);

  useEffect(() => {
    const fetchProducts = async () => {
      setLoading(true);
      try {
        const response = await fetch(
          `https://api.example.com/products?page=${currentPage}`
        );
        const data = await response.json();
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
