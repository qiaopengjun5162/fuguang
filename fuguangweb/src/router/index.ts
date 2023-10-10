import {createRouter, createWebHistory, Router, RouteRecordRaw} from "vue-router";

// 路由列表
// RouterRecordRaw是路由组件对象
const routes: RouteRecordRaw[] = [
    {
        meta: {
            title: "浮光在线教育-首页",
            keepAlive: true
        },
        path: '/',         // uri访问地址
        name: "Home",
        component: () => import("../views/Home.vue")
    },
    {
        meta: {
            title: "浮光在线教育-用户登录",
            keepAlive: true
        },
        path: '/login',      // uri访问地址
        name: "Login",
        component: () => import("../views/Login.vue")
    }
]

// 路由对象实例化
const router: Router = createRouter({
    // history, 指定路由的模式
    history: createWebHistory(import.meta.env.BASE_URL),
    // 路由列表
    routes,
});


// 暴露路由对象
export default router