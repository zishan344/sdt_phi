import { useEffect, useState } from "react";
import apiClint from "../services/api-clint";

const useFetchCategories = () => {
  const [categories, setCategories] = useState([]);
  const [CategoryLoading, setCategoryLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCategories = async () => {
      setCategoryLoading(true);
      try {
        const response = await apiClint.get(`/categories`);
        const data = await response.data;
        setCategories(data);
      } catch (error) {
        setError(error);
      } finally {
        setCategoryLoading(false);
      }
    };
    fetchCategories();
  }, []);

  return { categories, loading: CategoryLoading, error };
};

export default useFetchCategories;
