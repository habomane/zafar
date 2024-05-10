import DEV_ENDPOINTS from '../endpoints'
export class PostService {
    async createPost(newPost)
    {
        const requestDate = new Date()
        const fetch_response = await fetch(DEV_ENDPOINTS.CREATE_POST, {
            method: "POST",
            body: JSON.stringify({
              title: newPost.title,
              description: newPost.description,
              date: requestDate, 
              ownerUuid: "",
              topicKey: newPost.topicKey

            }),
            headers: {
              "Content-type": "application/json; charset=UTF-8"
            }
        })
        const response = await fetch_response.json()
        return response

    }
}