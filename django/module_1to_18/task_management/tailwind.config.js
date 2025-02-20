/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // Templates at the project level
    "./**/templates/**/*.html", // Template  inside apps
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
