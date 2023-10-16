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
        component: () => import("../views/Login.vue")  // uri绑定的组件页面
    }
]

// 路由对象实例化
const router: Router = createRouter({
    // history, 指定路由的模式
    history: createWebHistory(import.meta.env.BASE_URL),
    // 路由列表
    routes,
});

// 客户端权限验证写在路由守卫里面
// 服务端的验证，分2块，1块在客户端的axios附带token，另1块在api服务端的视图中调用permission

router.beforeEach((to, from) => {
    document.title = to.meta.title
    // 返回 false 以取消导航
    // return false
})


// 暴露路由对象
export default router