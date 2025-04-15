import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation";
import { Swiper, SwiperSlide } from "swiper/react";
import { useState } from "react";
import { Navigation, Thumbs } from "swiper/modules";
import defaultImage from "../../assets/default_product.jpg";
const ProductImageGallery = ({ images, ProductName }) => {
  const [thumbsSwiper, setThumbsSwiper] = useState(null);
  const displayImages = images.length > 0 ? images : [{ image: defaultImage }];
  return (
    <div className="rounded-lg border overflow-hidden">
      <Swiper
        modules={[Navigation, Thumbs]}
        navigation
        thumbs={{
          swiper:
            thumbsSwiper && !thumbsSwiper?.destroyed ? thumbsSwiper : null,
        }}
        className="product-main-slider">
        {displayImages.map((image, index) => (
          <SwiperSlide key={index}>
            <div className="aspect-square bg-base-100">
              <img
                className="h-full w-full object-contain"
                src={image.image}
                alt={ProductName}
              />
            </div>
          </SwiperSlide>
        ))}
      </Swiper>
    </div>
  );
};

export default ProductImageGallery;
