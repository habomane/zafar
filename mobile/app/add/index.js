
import { useLocalSearchParams } from 'expo-router';
import { Link } from 'expo-router';
import { SafeAreaView, Text, View, ScrollView, StyleSheet} from 'react-native';

import Footer from '../../utils/footer';
import Header from '../../utils/header';

export default function AddScreen() {

  return (
    <View style={styles.main}>
    <Header style={styles.header}/>
    <View style={styles.body}>
    <ScrollView>
    <Text>This is to add a new post</Text>
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
},
main : {
  flex: 1, 
}, 
header: {
  paddingHorizontal: 15
},
body : {
  flex: 8,
  paddingHorizontal: 15
},
footer: {
  flex: 10,
  paddingHorizontal: 15
}
})