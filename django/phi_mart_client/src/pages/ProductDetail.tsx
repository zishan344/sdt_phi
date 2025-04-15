import AddToCartButton from "../components/productDetails/AddToCartButton";
import ProductImageGallery from "../components/productDetails/ProductImageGallery";

const ProductDetail = () => {
  const product = {
    id: 1,
    name: "Smartphone",
    description: "High-quality smartphone for everyday use.",
    price: 213.8,
    stock: 157,
    category: 1,
    price_with_tax: 235.18,
    images: [
      {
        id: 1,
        image:
          "https://res.cloudinary.com/dke0wkcio/image/upload/v1741432159/newwxwp9qtyjm5dk81yn.jpg",
      },
      {
        id: 2,
        image:
          "https://res.cloudinary.com/dke0wkcio/image/upload/v1741433037/cklqohh39wfpacojwp2i.png",
      },
    ],
  };
  return (
    <div className="w-3/4 mx-auto px-4 py-8">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:gap-12">
        <ProductImageGallery
          ProductName={product.name}
          images={product.images}
        />
        <div className="mt-auto">
          <AddToCartButton product={product} />
        </div>
      </div>
    </div>
  );
};

export default ProductDetail;
