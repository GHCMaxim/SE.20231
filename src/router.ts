import { createRouter, createWebHistory } from "vue-router";
import FinanceManager from "./pages/FinanceManager/_FinanceManager.vue";
import Home from "./pages/HomePage/_HomePage.vue";
import HouseManager from "./pages/HouseManager/_HouseManager.vue";
import Login from "./pages/LoginPage.vue";
import Register from "./pages/RegisterPage.vue";
import Search from "./pages/SearchPage.vue";
import Statistics from "./pages/StatisticsPage.vue";
import Rewards from "./pages/Rewards/_RewardsPage.vue";

const routes = [
	{ path: "/", component: Home },
	{ path: "/finance-manager", component: FinanceManager },
	{ path: "/household-manager", component: HouseManager },
	{ path: "/login", component: Login },
	{ path: "/register", component: Register },
	{ path: "/search", component: Search },
	{ path: "/statistics", component: Statistics },
	{ path: "/rewards", component: Rewards },
];

export default createRouter({
	history: createWebHistory(),
	routes,
});
