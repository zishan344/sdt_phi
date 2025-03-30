import apiClint from "../../services/api-clint";
import { useEffect, useState } from "react";
import ProductItem from "./ProductItem";
import { Swiper, SwiperSlide } from "swiper/react";
import { Navigation } from "swiper/modules";
import "swiper/css";
import "swiper/css/navigation";
const Products = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    apiClint
      .get("/products")
      .then((res) => setProducts(res.data.results))
      .catch((err) => setError(err))
      .finally(() => setLoading(false));
  }, []);
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
        {!loading && !error && products.length === 0 && (
          <div className="flex justify-center items-center h-32">
            <p>No products found</p>
          </div>
        )}
        {!loading && !error && products.length > 0 && (
          <div className="">
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-2xl md:text-3xl font-semibold">
                Trending Products
              </h2>
              <a href="#" className="btn btn-secondary  rounded-full text-lg">
                View All
              </a>
            </div>
            <Swiper
              modules={[Navigation]}
              spaceBetween={10}
              slidesPerView={1}
              breakpoints={{
                640: { slidesPerView: 2 },
                1024: { slidesPerView: 3 },
              }}
              navigation
              className="mt-6">
              {products.map((product) => (
                <SwiperSlide key={product.id} className="flex justify-center">
                  <ProductItem key={product.id} product={product} />
                </SwiperSlide>
              ))}
            </Swiper>
          </div>
        )}
      </div>
    </section>
  );
};

export default Products;
