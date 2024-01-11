import { inject } from "vue";
import type { VueCookies } from "vue-cookies";
import { createRouter, createWebHistory } from "vue-router";
import FinanceManager from "./pages/FinanceManager/_FinanceManager.vue";
import Home from "./pages/HomePage/_HomePage.vue";
import HouseManager from "./pages/HouseManager/_HouseManager.vue";
import Login from "./pages/LoginPage.vue";
import Register from "./pages/RegisterPage.vue";
import Search from "./pages/SearchPage.vue";
import Statistics from "./pages/StatisticsPage.vue";
import Rewards from "./pages/Rewards/_RewardsPage.vue";
import parseToken from "./parseToken";

const routes = [
	{ path: "/", component: Home, name: "Home" },
	{
		path: "/finance-manager",
		component: FinanceManager,
		name: "FinanceManager",
	}, // 0, 2
	{
		path: "/household-manager",
		component: HouseManager,
		name: "HouseManager",
	}, // 1, 2
	{ path: "/login", component: Login, name: "Login" },
	{ path: "/register", component: Register, name: "Register" },
	{ path: "/search", component: Search, name: "Search" },
	{ path: "/statistics", component: Statistics, name: "Statistics" },
	{ path: "/rewards", component: Rewards, name: "Rewards" }, // 0, 1
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

router.beforeEach((to, _, next) => {
	switch (to.name) {
		case "FinanceManager":
			if (!parseToken([0, 2])) return;
			break;
		case "HouseManager":
			if (!parseToken([1, 2])) return;
			break;
		case "Rewards":
			if (!parseToken([0, 1])) return;
			break;
		default:
			break;
	}
	next();
});

router.beforeEach((to, _, next) => {
	const $cookies = inject<VueCookies>("$cookies");
	const token = $cookies!.get("token");
	if (!token && to.name != "Login" && to.name != "Register")
		next({ name: "Login" });
	else next();
});

export default router;
