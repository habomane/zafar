
import { useLocalSearchParams } from 'expo-router';
import { Link } from 'expo-router';
import {  useFonts, Roboto_900Black, Roboto_700Bold} from '@expo-google-fonts/roboto';
import { SafeAreaView, TextInput, Text, View, ScrollView, StyleSheet} from 'react-native';
import Footer from '../../utils/footer';
import {Picker} from '@react-native-picker/picker';
import Header from '../../utils/header';
import { useState } from 'react';

export default function AddScreen() {
  let [fontsLoaded] = useFonts({
    Roboto_900Black, Roboto_700Bold
  });
  const [selectedLanguage, setSelectedLanguage] = useState();
  if (!fontsLoaded) {
    return null;
  }


  return (
    <View style={styles.main}>
    <Header style={styles.header}/>
    <View style={styles.body}>
    <ScrollView>
      <View style={styles.container}>
        <Text style={styles.textHead}>New Post</Text>
        <View style={styles.row}>
        <Text>Title here:</Text> 
         <TextInput 
         placeholder="Title"
         style={[styles.input, styles.inputText]}></TextInput>
        </View>
        <View style={styles.description}>
        <Text>Description here:</Text> 
         <TextInput style={[styles.input, styles.inputDescription]}
              multiline={true}
              placeholder="Details"
              ></TextInput>
        </View>
        <View style={styles.row}>
        <Picker
        style={{flex:1, height: 10}}
        selectedValue={selectedLanguage}
        onValueChange={(itemValue, itemIndex) => setSelectedLanguage(itemValue)}
      >
        <Picker.Item label="Select an option..." value="" />
        <Picker.Item label="Option 1" value="option1" />
        <Picker.Item label="Option 2" value="option2" />
        <Picker.Item label="Option 3" value="option3" />
      </Picker>
        </View>
      </View>
    </ScrollView>
    </View>
    <Footer style={styles.footer}/>
    </View>
  )

}

const styles = StyleSheet.create({
main : {
  flex: 1, 
}, 
header: {
  paddingHorizontal: 15
},
row : {
  flex: 1, 
  flexDirection: "row",
  width: "100%",
  justifyContent: "space-between",
  marginBottom: 10
},
inputText: {
  width: '81%'
},
input: {
  backgroundColor: "#ededed",
  width: "100%",
padding: 1,
borderRadius: 7, 
borderColor: "#d3d3d3",
borderWidth: 1
},
inputDescription : {
  height: 150
},
body : {
  flex: 8,
  paddingHorizontal: 15
},
description : {
  textAlign: "left",
  width: "100%",
  marginBottom: 20
},
textHead: {
fontFamily: "Roboto_700Bold",
fontSize: 26,
letterSpacing: 2,
marginBottom: 20
},
container: {
flex: 4,
alignItems: 'center'
},
footer: {
  flex: 10,
  paddingHorizontal: 15
}
})