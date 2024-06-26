
import { useLocalSearchParams } from 'expo-router';
import { Link } from 'expo-router';
import { SafeAreaView, Text, View, ScrollView, StyleSheet} from 'react-native';
import Footer from '../utils/footer';
import Header from '../utils/header';
import PostCard from '../components/postcard';
import { PostService } from '../services/postservice';
import { useEffect, useState } from 'react';

export default function HomeScreen() {
  const [allPosts, setAllPosts] = useState([]);
  const postService = new PostService()

  useEffect( () => {
    async function fetchData() {
      const posts = await postService.getPosts();
      setAllPosts(posts)
    }
    fetchData()
  }, [])

  return (
    <View style={styles.main}>
    <Header style={styles.header}/>
    <View style={styles.body}>
    <ScrollView>
      {allPosts.map((item, index) => (
        <View key={index}>
          <PostCard post={item}></PostCard>
        </View>
      ))}
    </ScrollView>
    </View>
    <Footer style={styles.footer}/>
    </View>
  )

}

const styles = StyleSheet.create({
background : {
  flex: 1,
  paddingHorizontal: '10px'
},container : {
flex: 1
},
main : {
  flex: 1, 
}, 
header: {
  flex: 1, 
  paddingHorizontal: 15
},
body : {
  flex: 8,
  paddingHorizontal: 15
},
footer: {
  flex: 1,
  paddingHorizontal: 15
}
})