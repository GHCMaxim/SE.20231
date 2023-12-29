/** @type {import('tailwindcss').Config} */

export default{
    plugins: [require('@pinegrow/tailwindcss-plugin').default,],
    get content() {
        const _content = [
        './index.html',
        './src/**/*.{html,vue,svelte,astro,js,cjs,ts,cts,mts,jsx,tsx,md,mdx}',
        //...
        ]
        return process.env.NODE_ENV === 'production'
        ? _content
        : [..._content, './_pginfo/**/*.{html,js}'] // used by Vue Designer Desginer for live-designing during development
  },
}

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
