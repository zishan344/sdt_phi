import { FaShoppingCart, FaTags } from "react-icons/fa";
import { MdVerified } from "react-icons/md";
import { BsShieldLock } from "react-icons/bs";

const Feature = () => {
  const features = [
    {
      icon: <FaShoppingCart className="text-red-400 text-4xl" />,
      title: "Free Delivery",
      description:
        "Get your orders delivered at no extra cost, fast and hassle-free.",
    },
    {
      icon: <MdVerified className="text-red-400 text-4xl" />,
      title: "Quality Guarantee",
      description:
        "We ensure top-notch quality for every product you purchase.",
    },
    {
      icon: <FaTags className="text-red-400 text-4xl" />,
      title: "Daily Offers",
      description: "Exclusive discounts and special deals available every day.",
    },
    {
      icon: <BsShieldLock className="text-red-400 text-4xl" />,
      title: "100% Secure Payment",
      description:
        "Your payment information is encrypted and completely secure.",
    },
  ];
  return (
    <div className="container mx-auto my-20">
      <section className="grid grid-cols-1 md:grid-cols-4 gap-4">
        {features.map((feature, index) => (
          <div
            key={index}
            className="flex flex-col items-center justify-center p-4 bg-white">
            <div className="p-3 bg-red-100 rounded-full">{feature.icon}</div>
            <h3 className="text-xl font-semibold mt-4">{feature.title}</h3>
            <p className="text-center text-gray-500 mt-2">
              {feature.description}
            </p>
          </div>
        ))}
      </section>
    </div>
  );
};

export default Feature;
