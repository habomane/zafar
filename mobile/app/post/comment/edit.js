
import { useLocalSearchParams } from "expo-router";
import { Link } from "expo-router";
import { Text, View } from "react-native";

export default function CommentEditScreen() {
  const { slug } = useLocalSearchParams();

  return (
    <View>
      <Text>Topic</Text>
      <Link href="/">Go back </Link>
    </View>
  );
}
