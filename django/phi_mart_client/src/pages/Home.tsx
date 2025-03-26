import HeroCarousel from "../components/carousel/HeroCarousel";
import Category from "../components/Categories/Category";
import Feature from "../components/Feature";
import Products from "../components/Products/Products";

const Home = () => {
  return (
    <div>
      <HeroCarousel />
      <Feature />
      <Category />
      <Products />
    </div>
  );
};

export default Home;
