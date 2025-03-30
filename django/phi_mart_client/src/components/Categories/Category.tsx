import CategoryItem from "./CategoryItem";
import apiClint from "../../services/api-clint";
import { useEffect, useState } from "react";
const Category = () => {
  const [categories, setCategories] = useState([]);
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
  console.log(categories);
  return (
    <section>
      <div className="container mx-auto px-4 py-8">
        {loading && (
          <div className="flex justify-center items-center h-32">
            <div className="loader">Loading</div>
          </div>
        )}

        {error && (
          <div className="flex justify-center items-center h-32">
            <p className="text-red-500">Error: {error.message}</p>
          </div>
        )}
        {!loading && !error && categories.length === 0 && (
          <div className="flex justify-center items-center h-32">
            <p>No categories found</p>
          </div>
        )}
        {!loading && !error && categories.length > 0 && (
          <div className="">
            <div className="flex justify-between gap-3 items-center mb-4">
              <h2 className="text-2xl md:text-3xl font-semibold">
                Browse Categories
              </h2>
              <button className="btn btn-secondary rounded-full">
                View All
              </button>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
              {categories.map((category, index) => (
                <CategoryItem
                  key={category?.id}
                  index={index}
                  category={category}
                />
              ))}
            </div>
          </div>
        )}
      </div>
    </section>
  );
};

export default Category;
