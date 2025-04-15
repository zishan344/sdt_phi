import { useState } from "react";
import { FaCheck, FaShoppingCart } from "react-icons/fa";
import { FaMinus, FaPlus } from "react-icons/fa6";
import useCartContext from "../../hooks/useCartContext";

const AddToCartButton = ({ product }) => {
  const [quantity, setQuantity] = useState(1);
  const [isAdded, setIsAdded] = useState(false);
  const [isAdding, setIsAdding] = useState(false);
  const { AddCartItems } = useCartContext();
  const increaseQuantity = () => {
    if (quantity < product.stock) {
      setQuantity(quantity + 1);
    }
  };

  const decreaseQuantity = () => {
    if (quantity > 1) {
      setQuantity(quantity - 1);
    }
  };

  const addToCart = async () => {
    setIsAdding(true);
    try {
      await AddCartItems(product.id, quantity);
      setIsAdded(true);
      setIsAdding(false);
    } catch (error) {
      console.log(error);
      setIsAdding(false);
    }
  };

  return (
    <div className="space-y-4">
      <div className="join">
        <button
          className="btn btn-outline join-item"
          onClick={decreaseQuantity}
          disabled={quantity <= 1}>
          <FaMinus className="h-4 w-4" />
        </button>
        <input
          type="number"
          value={quantity}
          min={1}
          max={product?.stock}
          className="input input-bordered join-item w-16 text-center [appearance:textfield] [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:appearance-none"
        />
        <button
          className="btn btn-outline join-item"
          onClick={increaseQuantity}
          disabled={quantity >= product.stock}>
          <FaPlus className="h-4 w-4" />
        </button>
      </div>
      <button
        onClick={addToCart}
        disabled={isAdded || isAdding || product.stock === 0}
        className="btn btn-primary w-full">
        {isAdding ? (
          <span className="flex items-center">
            <span className="loading loading-spinner loading-ms mr-2">
              Adding...
            </span>
          </span>
        ) : isAdded ? (
          <span className="flex items-center">
            <FaCheck className="mr-2 h-4 w-4" />
            Added to Cart
          </span>
        ) : (
          <span className="flex items-center">
            <FaShoppingCart className="mr-2 h-4 w-4" />
            Add to Cart
          </span>
        )}
      </button>
    </div>
  );
};

export default AddToCartButton;
