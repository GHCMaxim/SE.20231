/** @type {import('tailwindcss').Config} */

module.exports = {
	content: ["./src/**/*.vue", "./public/index.html"],
	theme: {
		extend: {},
	},
	plugins: [require("daisyui")],
	daisyui: {
		themes: [
			{
				mytheme: {
					primary: "#5669cc",
					secondary: "#ffffff",
					accent: "#ffffff",
					neutral: "#ffffff",
					"base-100": "#ffffff",
					info: "#ffffff",
					success: "#00ffff",
					warning: "#ffffff",
					error: "#ffffff",
				},
			},
		],
	},
};
