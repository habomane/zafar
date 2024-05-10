import { useLocalSearchParams } from "expo-router";
import { SelectList } from "react-native-dropdown-select-list";
import { Link } from "expo-router";
import {
  useFonts,
  Roboto_900Black,
  Roboto_700Bold,
  Roboto_400Regular,
  Roboto_500Medium
} from "@expo-google-fonts/roboto";
import {
  SafeAreaView,
  TextInput,
  Text,
  View,
  ScrollView,
  StyleSheet,
} from "react-native";
import Footer from "../../utils/footer";
import Header from "../../utils/header";
import { useState } from "react";
import React from "react";

export default function AddScreen() {
  let [fontsLoaded] = useFonts({
    Roboto_900Black,
    Roboto_700Bold,
    Roboto_400Regular,
    Roboto_500Medium
  });
  const [selected, setSelected] = React.useState("");

  const data = [
    { key: "1", value: "Mobiles" },
    { key: "2", value: "Appliances" },
    { key: "3", value: "Cameras" },
    { key: "4", value: "Computers" },
    { key: "5", value: "Vegetables" },
    { key: "6", value: "Diary Products" },
    { key: "7", value: "Drinks" },
  ];
  const [selectedLanguage, setSelectedLanguage] = useState();

  if (!fontsLoaded) {
    return null;
  }

  return (
    <View style={styles.main}>
      <Header style={styles.header} />
      <View style={styles.body}>
        <ScrollView>
          <View style={styles.container}>
            <Text style={styles.textHead}>New Post</Text>
            <View style={styles.row}>
              <Text style={styles.textBold}>Title here:</Text>
              <TextInput
                placeholder="Title"
                style={[styles.input, styles.inputText]}
              ></TextInput>
            </View>
            <View style={styles.description}>
              <Text style={styles.textBold}>Description here:</Text>
              <TextInput
                style={[styles.input, styles.inputDescription]}
                multiline={true}
                placeholder="Details"
              ></TextInput>
            </View>
            <View style={styles.selectContainer}>
            <Text style={styles.textBold}>Topic:</Text>
              <SelectList
                setSelected={(val) => setSelected(val)}
                data={data}
                save="value"
              />
            </View>

            <View style={styles.greenBtn}>
              <Text style={styles.whiteText}>Create Post</Text>
            </View>
          </View>
        </ScrollView>
      </View>
      <Footer style={styles.footer} />
    </View>
  );
}

const styles = StyleSheet.create({
  main: {
    flex: 1,
    justifyContent: "space-between"
  },
  header: {
    paddingHorizontal: 15,
  },
  row: {
    flex: 1,
    flexDirection: "row",
    width: "100%",
    justifyContent: "space-between",
    marginBottom: 10,
    alignItems: "center",
  },
  inputText: {
    width: "81%",
    height: 30,
  },
  greenBtn: {
    backgroundColor: "#00563B",
    padding: 10,
    marginTop: 30,
  },
  whiteText: {
    color: "white",
  },
  selectContainer: {
    width: "100%",
    gap: 5
  },
  input: {
    backgroundColor: "#ededed",
    width: "100%",
    padding: 1,
    borderRadius: 7,
    borderColor: "#d3d3d3",
    borderWidth: 1,
  },
  inputDescription: {
    height: 150,
  },
  body: {
    flex: 8,
    paddingHorizontal: 15,
  },
  description: {
    textAlign: "left",
    width: "100%",
    marginBottom: 20,
  },
  textHead: {
    fontFamily: "Roboto_700Bold",
    fontSize: 26,
    letterSpacing: 2,
    marginBottom: 20,
  },
  container: {
    flex: 4,
    alignItems: "center",
  },
  footer: {
    flex: 10,
    paddingHorizontal: 15,
  },
  textBase : {
    fontFamily: "Roboto_400Regular",
    fontSize: 14
  },
  textBold : {
    fontFamily: "Roboto_500Medium"
  }

});
