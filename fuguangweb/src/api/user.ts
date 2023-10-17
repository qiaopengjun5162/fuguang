import {reactive} from "vue";
import http from "../utils/http";

const user = reactive({
    account: "root", // 既可以是用户名、手机号，也可以是其他的唯一字段
    password: "123456", // 登录密码
    re_password: "",  // 确认密码
    remember: false, // 是否记住密码
    mobile: "",      // 登录手机号码
    sms_code: "",        // 验证码
    login_type: 0,   // 登录类型
    login(data) {
        // 用户登录
        return http.post("/users/login/", data)
    },
    check_mobile(mobile) {
        // 验证手机号
        return http.get(`/users/mobile/${mobile}/`)
    },
    register(data) {
        // 用户注册请求
        return http.post("/users/register/", data)
    }
})

export default user