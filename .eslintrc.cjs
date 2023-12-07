// @ts-check
const { defineConfig } = require("eslint-define-config");

/// <reference types="@eslint-types/typescript-eslint" />

module.exports = defineConfig({
	env: {
		browser: true,
		es2021: true,
	},
	extends: [
		"eslint:recommended",
		"@vue/typescript/recommended",
		"plugin:vue/vue3-recommended",
		"plugin:tailwindcss/recommended",
		"plugin:vue/vue3-essential",
		"plugin:prettier/recommended",
	],
	overrides: [
		{
			env: {
				node: true,
			},
			files: [".eslintrc.{js,cjs,mjs}"],
			parserOptions: {
				sourceType: "script",
			},
		},
	],
	parser: "vue-eslint-parser",
	parserOptions: {
		ecmaVersion: "latest",
		sourceType: "module",
		parser: "@typescript-eslint/parser",
	},
	plugins: ["vue"],
	rules: {
		"prettier/prettier": [
			"error",
			{
				"tabWidth": 4,
				"useTabs": true,
			}
		],
		"no-unused-vars": "off",
		"tailwindcss/no-custom-classname": "off",
	},
});
