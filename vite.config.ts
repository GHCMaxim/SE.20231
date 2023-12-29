import { rmSync } from "node:fs";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import electron from "vite-plugin-electron";
import renderer from "vite-plugin-electron-renderer";
import { notBundle } from "vite-plugin-electron/plugin";
import pkg from "./package.json";
import { liveDesigner } from '@pinegrow/vite-plugin';
import topLevelAwait from "vite-plugin-top-level-await";

// https://vitejs.dev/config/
export default defineConfig(({ command }) => {
	rmSync("dist-electron", { recursive: true, force: true });

	const isServe = command === "serve";
	const isBuild = command === "build";
	const sourcemap = isServe || !!process.env.VSCODE_DEBUG;

	return {
		plugins: [
			topLevelAwait({
				promiseExportName: "__tla",
				promiseImportName: i => `__tla_${i}`
			}),
            liveDesigner({
                tailwindcss: {
                    /* Please ensure that you update the filenames and paths to accurately match those used in your project. */
                    configPath: 'tailwind.config.js',
                    cssPath: '@/assets/css/tailwind.css',
                    // themePath: false, // Set to false so that Design Panel is not used
                    // restartOnConfigUpdate: true,
                    restartOnThemeUpdate: true,
                },
                 devServerUrls: {
                    /* Please ensure that you update this URL with the actual URL of your remote dev-server. */
                    network: 'http://localhost:5173', // If running a remote dev-server
                },
            }),
			vue(),
			electron([
				{
					// Main process entry file of the Electron App.
					entry: "electron/main/index.ts",
					onstart({ startup }) {
						if (process.env.VSCODE_DEBUG) {
							console.log(
								/* For `.vscode/.debug.script.mjs` */ "[startup] Electron App",
							);
						} else {
							startup();
						}
					},
					vite: {
						build: {
							sourcemap,
							minify: isBuild,
							target: "esnext",
							outDir: "dist-electron/main",
							rollupOptions: {
								// Some third-party Node.js libraries may not be built correctly by Vite, especially `C/C++` addons,
								// we can use `external` to exclude them to ensure they work correctly.
								// Others need to put them in `dependencies` to ensure they are collected into `app.asar` after the app is built.
								// Of course, this is not absolute, just this way is relatively simple. :)
								external: Object.keys(
									"dependencies" in pkg
										? pkg.dependencies
										: {},
								),
							},
						},
						esbuild: {
							target: "esnext"
						},
						optimizeDeps: {
							esbuildOptions: {
								target: "esnext"
							}
						},
						plugins: [
							// This is just an option to improve build performance, it's non-deterministic!
							// e.g. `import log from 'electron-log'` -> `const log = require('electron-log')`
							isServe && notBundle(),
						],
					},
				},
				{
					entry: "electron/preload/index.ts",
					onstart({ reload }) {
						// Notify the Renderer process to reload the page when the Preload scripts build is complete,
						// instead of restarting the entire Electron App.
						reload();
					},
					vite: {
						build: {
							sourcemap: sourcemap ? "inline" : undefined, // #332
							minify: isBuild,
							outDir: "dist-electron/preload",
							target: "esnext",
							rollupOptions: {
								external: Object.keys(
									"dependencies" in pkg
										? pkg.dependencies
										: {},
								),
							},
						},
						esbuild: {
							target: "esnext"
						},
						optimizeDeps: {
							esbuildOptions: {
								target: "esnext"
							}
						},
						plugins: [isServe && notBundle()],
					},
				},
			]),
			// Use Node.js API in the Renderer process
			renderer(),
		],
		clearScreen: false,
	};
});
