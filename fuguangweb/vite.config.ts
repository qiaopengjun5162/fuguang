import path from 'path'
import {defineConfig, loadEnv} from 'vite'
import vue from '@vitejs/plugin-vue'
import Icons from 'unplugin-icons/vite'
import IconsResolver from 'unplugin-icons/resolver'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import {ElementPlusResolver} from 'unplugin-vue-components/resolvers'
import Inspect from 'vite-plugin-inspect' // https://github.com/antfu/vite-plugin-inspect

const pathSrc = path.resolve(__dirname, 'src')

// https://vitejs.dev/config/
export default defineConfig({
    server: {
        port: 3000,           // 客户端的运行端口，此处也可以绑定vue运行的端口，当然也可以写在pycharm下
        host: 'www.fuguang.cn', // 客户端的运行地址，此处也可以绑定vue运行的域名，当然也可以写在pycharm下
        proxy: {
            // 字符串简写写法：http://localhost:5173/foo -> http://localhost:4567/foo
            // '/foo': 'http://localhost:4567',
            // '/foo': loadEnv("", process.cwd()).VITE_API_URL,
            // 带选项写法：http://localhost:5173/api/bar -> http://jsonplaceholder.typicode.com/bar
            '/api': {
                target: 'http://api.fuguang.cn:8000/',
                changeOrigin: true,
                 ws: true,    // 是否支持websocket跨域
                rewrite: (path) => path.replace(/^\/api/, ''),
            },
        }
    },
    resolve: {
        alias: {
            '@': pathSrc,
        },
    },
    plugins: [
        vue(),
        AutoImport({
            // global imports to register
            imports: [
                // presets
                'vue',
                'vue-router'
            ], // 自动导入 vue 相关函数，如 ref reactive toRef 等
            resolvers: [
                ElementPlusResolver(),

                // Auto import icon components
                // 自动导入图标组件
                IconsResolver({
                    // prefix: 'Icon',
                })
            ],
            eslintrc: {enabled: true}, // eslint 会报 no-undef 错误，添加此项会生成 .eslintrc-auto-import.json
            // 生成自动导入的TS声明文件
            dts: path.resolve(pathSrc, 'auto-imports.d.ts'),
        }),
        Components({
            resolvers: [
                // Auto register icon components
                // 自动注册图标组件
                IconsResolver({
                    enabledCollections: ['ep'],
                }),
                ElementPlusResolver()
            ], // 自动导入 Element Plus 组件，图标组件
            dts: path.resolve(pathSrc, 'components.d.ts'),
        }),
        Icons({
            autoInstall: true,
        }),

        Inspect(),
    ],
})
