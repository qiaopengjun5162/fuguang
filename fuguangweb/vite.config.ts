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
