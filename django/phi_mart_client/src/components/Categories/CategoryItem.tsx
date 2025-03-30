const CategoryItem = ({ index, category }) => {
  const gradients: string[] = [
    "from-pink-100 to-blue-100",
    "from-blue-100 to-purple-100",
    "from-purple-100 to-pink-100",
    "from-pink-100 to-blue-100",
  ];
  return (
    <div
      className={`rounded-xl overflow-hidden shadow-sm hover:shadow-md transition-shadow duration-300 cursor-pointer bg-gradient-to-br px-4 py-2 ${
        gradients[index % gradients.length]
      }`}>
      <div className="flex justify-between gap-3 items-center mb-4">
        <div className="avatar avatar-placeholder">
          <div className="bg-secondary text-secondary-content w-8 rounded-full">
            <span className="text-lg font-semibold">
              {category.name.charAt(0)}
            </span>
          </div>
        </div>
        <button className="btn btn-sm rounded-full">
          {category.product_count} Items
        </button>
      </div>
      <div>
        <h2 className="text-2xl font-bold">{category.name}</h2>
        <p className="text-sm text-gray-500">{category.description}</p>
      </div>
      <div>
        <button className="pl-0 btn btn-link text-secondary no-underline mt-4">
          Explore {">"}{" "}
        </button>
      </div>
    </div>
  );
};

export default CategoryItem;
