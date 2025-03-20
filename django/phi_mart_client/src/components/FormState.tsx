import { FormEvent, useState } from "react";

const FormState = () => {
  const personObj = { name: "", age: "" };
  const [person, setPerson] = useState(personObj);

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log(person);
  };

  return (
    <div className="w-1/2 mx-auto">
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label
            htmlFor="name"
            className="block text-gray-700 text-sm font-bold mb-2">
            Name:
          </label>
          <input
            id="name"
            type="text"
            value={person.name}
            onChange={(event) =>
              setPerson({ ...person, name: event.target.value })
            }
            className="w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 rounded-md"
          />
        </div>

        <div className="mb-3">
          <label
            htmlFor="age"
            className="block text-gray-700 text-sm font-bold mb-2">
            Age:
          </label>
          <input
            id="age"
            type="number"
            value={person.age}
            onChange={(event) =>
              setPerson({ ...person, age: event.target.value })
            }
            className="w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 rounded-md"
          />
        </div>

        <button
          type="submit"
          className="px-3 py-2 text-white bg-blue-500 rounded-md">
          Submit
        </button>
      </form>
    </div>
  );
};

export default FormState;
