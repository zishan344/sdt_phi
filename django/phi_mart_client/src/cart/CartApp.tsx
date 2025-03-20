import { Trash2 } from "lucide-react";
import { useState } from "react";
import { SubmitHandler, useForm } from "react-hook-form";
import { CartForm, CartItem } from "./type";

const CartApp = () => {
  const { register, handleSubmit } = useForm<CartForm>();
  const [cart, setCart] = useState<CartItem[]>([]);

  /*
    const cart = [
    { name: "Laptop", price: 34000 },
    { name: "Mobile Phone", price: 20000 },
  ]; 

  {product1: Laptop, product2: "MObile"}
  */

  //   Add Item
  const addItem: SubmitHandler<CartForm> = (data: CartForm) => {
    const existingItem = cart.find((item: CartItem) => item.name === data.name);

    if (existingItem) {
      setCart(
        cart.map((item: CartItem) =>
          item.name === data.name
            ? { ...item, quantity: item.quantity + 1 }
            : item
        )
      );
    } else {
      setCart([
        ...cart,
        { name: data.name, price: Number(data.price), quantity: 1 },
      ]);
    }
  };

  // Increase Quantity
  const increaseQuantity = (name: string) => {
    setCart(
      cart.map((item: CartItem) =>
        item.name === name ? { ...item, quantity: item.quantity + 1 } : item
      )
    );
  };

  // Increase Quantity
  const decreaseQuantity = (name: string) => {
    setCart(
      cart
        .map((item: CartItem) =>
          item.name === name ? { ...item, quantity: item.quantity - 1 } : item
        )
        .filter((item) => item.quantity > 0)
    );
  };

  // Remove Item
  const RemoveItem = (name: string) => {
    setCart(cart.filter((item: CartItem) => item.name !== name));
  };

  // Calculate total price
  const totalPrice = cart.reduce(
    (total: number, item: CartItem) => total + item.price * item.quantity,
    0
  );

  return (
    <div className="w-2/3 mx-auto bg-gray-100 rounded-lg p-6 shadow-md">
      {/* Add Cart Items  */}
      <form onSubmit={handleSubmit(addItem)} className="mb-4 space-y-2">
        <input
          {...register("name", { required: true })}
          type="text"
          placeholder="Item Name"
          className="border p-2 rounded w-full"
        />
        <input
          {...register("price", { required: true })}
          type="number"
          placeholder="Item Price"
          className="border p-2 rounded w-full"
        />
        <button className="bg-blue-500 text-white px-4 py-2 rounded w-full">
          Add Item
        </button>
      </form>

      {/* Cart Items List  */}
      {cart.length > 0 ? (
        // Todo cart items
        <div>
          {cart.map((item) => (
            <div
              key={item.name}
              className="flex justify-between items-center p-2  bg-white rounded mb-2">
              <p className="font-semibold">{item.name}</p>
              <p className="text-sm text-gray-600">
                {(item.price * item.quantity).toFixed(2)}
              </p>

              <div className="flex items-center">
                <button
                  onClick={() => decreaseQuantity(item.name)}
                  className="bg-red-500 text-white px-2 py-1 rounded">
                  -
                </button>
                <span className="mx-2">{item.quantity}</span>
                <button
                  onClick={() => increaseQuantity(item.name)}
                  className="bg-green-500 text-white px-2 py-1 rounded">
                  +
                </button>
              </div>

              <button onClick={() => RemoveItem(item.name)}>
                <Trash2 />
              </button>
            </div>
          ))}

          {/* Total Price  */}
          <div className="mt-4 font-bold text-lg">
            Total: ${totalPrice.toFixed(2)}
          </div>
        </div>
      ) : (
        <p>No Cart Items</p>
      )}
    </div>
  );
};

export default CartApp;
