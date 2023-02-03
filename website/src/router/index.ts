import { createRouter, createWebHistory } from 'vue-router'
import HomePage from "@/views/HomePage.vue";
import About from "@/views/About.vue";
import SignUp from "@/views/SignUp.vue";
import Login from "@/views/Login.vue";
import Diagnose from "@/views/DiagnoseUser.vue"

import Obesity from '@/views/diagnose/Obesity.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomePage,
    },
    {
      path: '/about',
      name: "about",
      component: About,
    },
    {
      path: "/signUp",
      name: "signUp",
      component: SignUp,
    },
    {
      path: "/login",
      name: "login",
      component: Login,
    },
    {
      path: "/diagnose",
      name: "diagnose",
      component: Diagnose,
    },
		{
			path: "/diagnose-obesity",
			name: "diagnoseDisease-obesity",
			component: Obesity
		}
  ],
});

export default router;
