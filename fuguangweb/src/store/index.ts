import {createStore} from "vuex"
import createPersistedState from "vuex-persistedstate"

// 实例化一个vuex存储库
export default createStore({
     // 调用永久存储vuex数据的插件，localstorage里会多一个名叫vuex的Key，里面就是vuex的数据
    plugins: [createPersistedState()],
    state () {  // 数据存储位置，相当于组件中的data
        return {
          user: {

          }
        }
    },
    mutations: { // 操作数据的方法，相当于methods
        login (state, user) {  // state 就是上面的state   state.user 就是上面的数据
          state.user = user
        }
    }
})