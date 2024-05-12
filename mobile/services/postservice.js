import { DEV_ENDPOINTS } from "../endpoints"
export class PostService {

    async getPosts()
    {
        const response = await fetch(DEV_ENDPOINTS.GET_POSTS, {
            method: "GET",
            headers: {
                "Content-type": "application/json; charset=UTF-8",
                "Accept": "application/json",
                "Accept-Encoding": "gzip, deflate, br"
            }
        })
        const responseData = await response.json()
        return responseData
    }

    async getPost(postKey)
    {
        const response = await fetch(DEV_ENDPOINTS.GET_POST_FROM_POSTKEY + postKey, {
            method: "GET",
            headers: {
                "Content-type": "application/json; charset=UTF-8",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br"
            }
        })
        const responseData = await response.json()
        return responseData
    }

    async createPost(newPost)
    {
        const body = JSON.stringify(newPost.postJson())
        const response = await fetch(DEV_ENDPOINTS.CREATE_POST, {
            method: "POST",
            body: body,
            headers: {
                "Content-type": "application/json",
                "Accept": "application/json",
                "Accept-Encoding": "gzip, deflate, br"
            }
        })
        const responseData = await response.json()
        return responseData

    }
}