import CategoryItem from "./CategoryItem";
import apiClint from "../../services/api-clint";
import { useEffect, useState } from "react";
const Category = () => {
  const [category, setCategories] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    apiClint
      .get("/categories")
      .then((res) => setCategories(res.data))
      .catch((err) => setError(err))
      .finally(() => setLoading(false));
  }, []);

  return (
    <section>
      <div className="container mx-auto px-4 py-8">
        <div className="flex justify-between gap-3 items-center mb-4">
          <h2 className="text-4xl">Browse Categories</h2>
          <button className="btn btn-secondary rounded-full">View All</button>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <CategoryItem />
          <CategoryItem />
          <CategoryItem />
          <CategoryItem />
        </div>
      </div>
    </section>
  );
};

export default Category;
