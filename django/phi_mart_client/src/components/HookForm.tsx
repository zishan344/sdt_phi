import { SubmitHandler, useForm } from "react-hook-form";
import { FormValues } from "./types";

const HookForm = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormValues>();
  const onSubmit: SubmitHandler<FormValues> = (data) => console.log(data);

  return (
    <div className="w-1/2 mx-auto">
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="mb-3">
          <label
            htmlFor="name"
            className="block text-gray-700 text-sm font-bold mb-2">
            Name:
          </label>
          <input
            id="name"
            type="text"
            {...register("name", { required: true, minLength: 5 })}
            className="w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 rounded-md"
          />
          {errors.name?.type === "required" && (
            <span>This Field Is required</span>
          )}
          {errors.name?.type === "minLength" && (
            <span>Minimum length is 5</span>
          )}
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
            {...register("age", { required: true, min: 18 })}
            className="w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 rounded-md"
          />
          {errors.age?.type === "required" && (
            <span>This Field Is required</span>
          )}
          {errors.age?.type === "min" && <span>Minimum age is 18</span>}
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

export default HookForm;
