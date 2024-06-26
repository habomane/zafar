export class CreatePost
{
    constructor(title, description, topicKey, ownerUuid)
    {
        this.title = title
        this.description = description
        this.topicKey = topicKey
        this.ownerUuid = ownerUuid
    }

    postJson(){
        const requestDate = new Date()
        return {
                "title": this.title,
                "description": this.description,
                "date": requestDate,
                "ownerUuid": this.ownerUuid,
                "topicKey": this.topicKey
              }


    }
}

export class Post {
    constructor(title, description, author, topic, date)
    {
        this.title = title
        this.description = description
        this.author = author
        this.topic = topic
        this.topic = date
    }
}