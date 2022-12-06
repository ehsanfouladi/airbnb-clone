/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html'],
  theme: {
    extend: {
        spacing:{
            "25vh": "25vh",
            "75vh":"75vh",
            "50vh":"50vh"
        },
        borderRadius:{
            xl : "1.5rem"
        }
    },
  },
  plugins: [],
}
