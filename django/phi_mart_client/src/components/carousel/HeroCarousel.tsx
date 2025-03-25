import CarouselSlide from "./CarouselSlide";
import book from "../../assets/image/book.png";
import fashion from "../../assets/image/fashion.png";
import technology from "../../assets/image/technology.png";
import { Swiper, SwiperSlide } from "swiper/react";
import { Autoplay, Pagination, Navigation } from "swiper/modules";
// Import Swiper styles
import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation";
const HeroCarousel = () => {
  const slides = [
    {
      title: "This Fine Print Book Collections",
      subtitle: "Discount available. Grab it now!",
      image: book,
    },
    {
      title: "Exclusive Fashion Collections",
      subtitle: "A specialists label creating luxury essentials!",
      image: fashion,
    },
    {
      title: "Your Digital World, Connected.",
      subtitle: "Explore a range of devices for seamless living.",
      image: technology,
    },
  ];

  return (
    <div>
      <Swiper
        spaceBetween={30}
        centeredSlides={true}
        autoplay={{
          delay: 2500,
          disableOnInteraction: false,
        }}
        pagination={{
          clickable: true,
        }}
        navigation={true}
        modules={[Autoplay, Pagination, Navigation]}
        className="mySwiper">
        {slides.map((slide, index) => (
          <SwiperSlide key={index}>
            <CarouselSlide
              title={slide.title}
              subtitle={slide.subtitle}
              image={slide.image}
            />
          </SwiperSlide>
        ))}
      </Swiper>
    </div>
  );
};

export default HeroCarousel;
