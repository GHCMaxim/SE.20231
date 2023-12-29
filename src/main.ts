import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import VueCookies from "vue-cookies";
import router from "./router";

const app = createApp(App);

app.use(router);
app.use(VueCookies, { expires: "7d" });

app.mount("#app");

export default app;
