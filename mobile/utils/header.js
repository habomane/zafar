import { View, Text, StyleSheet, Image } from "react-native";
import { FontAwesome } from '@expo/vector-icons';
import { Link } from "expo-router";

export default function Header({ style }) {
  return (
    <View style={[style, styles.header]}>
        <View style={styles.headerContainer}>
        <Link href='/navigation'><FontAwesome name="navicon" size={34} color="black" /></Link>
        <View  style={styles.img}>
        <Link href='/profile'><Image source={require('../images/png/user.png')} /></Link>
        </View>
        </View>
    </View>
  );
}

const styles = StyleSheet.create({
  header: {
    flex: 1,
  },
  headerContainer : {
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 25
  }
});
