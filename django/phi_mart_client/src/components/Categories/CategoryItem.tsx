const CategoryItem = () => {
  return (
    <div className="shadow-lg bg-base-100 rounded-lg p-4 flex flex-col justify-between h-full">
      <div className="flex justify-between gap-3 items-center mb-4">
        <div className="avatar avatar-placeholder">
          <div className="bg-secondary text-secondary-content w-8 rounded-full">
            <span className="text-xs">U</span>
          </div>
        </div>
        <button className="btn btn-sm rounded-full">10 Items</button>
      </div>
      <div>
        <h2 className="text-2xl font-bold">Category Name</h2>
        <p className="text-sm text-gray-500">Category Description</p>
      </div>
      <div>
        <button className="btn btn-link text-secondary no-underline mt-4">
          Explore {">"}{" "}
        </button>
      </div>
    </div>
  );
};

export default CategoryItem;
