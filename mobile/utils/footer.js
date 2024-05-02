import { View, Text, StyleSheet } from "react-native"
import { Link } from "expo-router";
import { FontAwesome5 } from '@expo/vector-icons';
import { MaterialIcons } from '@expo/vector-icons';
import { FontAwesome } from '@expo/vector-icons';

export default function Footer({style})
{
    return (
    <View style={[style, styles.footer]}>
       <View style={styles.footerContainer}>
        <Link href="/home"><FontAwesome5 name="home" size={32} color="white" /></Link>
        <Link href="/home"><MaterialIcons name="add" size={48} color="white" /></Link>
        <Link href="/home"><FontAwesome name="search" size={30} color="white" /></Link>
       </View>
    </View>)
}


styles = StyleSheet.create({
footer: {
    flex: 1,
    paddingVertical: 10,
    backgroundColor: '#00563B'
},
footerContainer: {
    marginTop: 10,
    flexDirection: 'row',
    justifyContent: 'space-around',
    alignItems: 'center'
}
})