import {createRouter, createWebHistory, Router, RouteRecordRaw} from "vue-router";

// 路由列表
// RouterRecordRaw是路由组件对象
const routes: RouteRecordRaw[] = []

// 路由对象实例化
const router: Router = createRouter({
    // history, 指定路由的模式
    history: createWebHistory(),
    // 路由列表
    routes,
});


// 暴露路由对象
export default router