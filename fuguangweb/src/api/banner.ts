import http from "../utils/http";
import { reactive} from "vue";


// type BannerList = [
//     {
//         "image": string,
//         "name": string,
//         "link": string,
//         "is_http": boolean
//     }
// ]
//
// export const getBannerList = () => {
//     return http<BannerList>({
//         method: "GET",
//         url: "/banner/"
//     })
// }

const banner = reactive({
    banner_list: [],
    get_banner() {
        return http.get("/banner/")
    }
})

export default banner;