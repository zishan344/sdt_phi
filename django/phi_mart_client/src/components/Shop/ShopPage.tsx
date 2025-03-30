import { useState } from "react";
import ProductList from "./ProductList";
import Pagination from "./Pagination";
import useFetchProduct from "../../hooks/useFetchProducts";
import FilterSection from "./FilterSection";
import useFetchCategories from "../../hooks/useFetchCategories";

const ShopPage = () => {
  const [currentPage, setCurrentPage] = useState(1);
  const [priceRange, setPriceRange] = useState([0, 100]);
  const [selectedCategory, setSelectedCategory] = useState("");
  const [searchQuery, setSearchQuery] = useState("");
  const [sortOrder, setSortOrder] = useState("asc");

  const { products, loading, error, totalPage } = useFetchProduct(
    currentPage,
    priceRange,
    selectedCategory,
    searchQuery,
    sortOrder
  );
  const { categories } = useFetchCategories();
  console.log(categories);
  const handlePriceChange = (index, value) => {
    setPriceRange((prev) => {
      const newRange = [...prev];
      newRange[index] = value;
      return newRange;
    });
    setCurrentPage(1);
  };
  console.log(searchQuery);
  return (
    <div className="container mx-auto px-4 py-10">
      <h1 className="text-3xl font-bold mb-8">Shop Our Products</h1>
      <FilterSection
        handlePriceChange={handlePriceChange}
        priceRange={priceRange}
        categories={categories}
        handleCategoryChange={setSelectedCategory}
        selectedCategory={selectedCategory}
        handleSearchQuery={setSearchQuery}
        searchQuery={searchQuery}
        handleSorting={setSortOrder}
        sortOrder={sortOrder}
      />
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
