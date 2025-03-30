import { useEffect, useState } from "react";
import apiClint from "../services/api-clint";

const useFetchProduct = (
  currentPage: number,
  priceRange: number[],
  selectedCategory: string,
  searchQuery: string,
  sortOrder: string
) => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [totalPage, setTotalPage] = useState(0);

  useEffect(() => {
    const fetchProducts = async () => {
      setLoading(true);
      const url = `/products?price__gt=${priceRange[0]}&price__lt=${priceRange[1]}&page=${currentPage}&category_id=${selectedCategory}&search=${searchQuery}&ordering=${sortOrder}`;
      try {
        const response = await apiClint.get(url);
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
  }, [currentPage, selectedCategory, priceRange, searchQuery, sortOrder]);

  return { products, loading, error, totalPage };
};

export default useFetchProduct;
