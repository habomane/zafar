import { View, Text, StyleSheet } from "react-native"

export default function PostCard({ post }) {
    return (
        <View style={styles.container}>
            <Text>{post.title}</Text>
            <Text>{ post.date }</Text>
            <Text>Author: { post.author }</Text>
            <Text>{ post.description }</Text>
            <Text>{ post.topic }</Text>
        </View>
    )
}


styles = StyleSheet.create({
    container: {
        flex: 1
    }
})
