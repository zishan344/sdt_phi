import { FormEvent, useRef } from "react";

const Form = () => {
  const nameRef = useRef(null);
  const ageRef = useRef(null);
  const person = { name: "", age: 0 };
  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (nameRef !== null) person.name = nameRef.current.value;
    if (ageRef !== null) person.age = ageRef.current.value;

    console.log(person);
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <div>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label
              className="block text-gray-700 text-sm font-bold mb-2"
              htmlFor="name">
              Name:
            </label>
            <input
              ref={nameRef}
              id="name"
              type="text"
              className="w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 rounded-md"
            />
          </div>
          <div className="mb-3">
            <label
              className="block text-gray-700 text-sm font-bold mb-2"
              htmlFor="age">
              Age:
            </label>
            <input
              ref={ageRef}
              id="age"
              type="number"
              className="w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 rounded-md"
            />
          </div>
          <button className="px-3 cursor-pointer py-2 text-white bg-blue-500 rounded-md">
            Submit
          </button>
        </form>
      </div>
    </div>
  );
};

export default Form;
