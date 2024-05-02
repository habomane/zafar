import { View, Text, StyleSheet } from "react-native"

export default function Header({style})
{
    return (<View style={[style, styles.header]}><Text>header here</Text></View>)
}


const styles = StyleSheet.create({
header : {
    flex: 1
}
})