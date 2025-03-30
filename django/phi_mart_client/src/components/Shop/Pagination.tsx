import React from "react";

const Pagination = ({ totalPage, currentPage, handlePageChange }) => {
  return (
    <div className="flex justify-center mb-6">
      {Array.from({ length: totalPage }, (_, i) => (
        <button
          key={i + 1}
          className={`mx-1 px-3 py-1 rounded ${
            currentPage === i + 1 ? "bg-secondary text-white" : "bg-gray-200"
          }`}>
          {i + 1}
        </button>
      ))}
    </div>
  );
};

export default Pagination;
