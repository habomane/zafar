
import { useLocalSearchParams } from "expo-router";
import { Link } from "expo-router";
import { Text, View } from "react-native";

export default function PostScreen() {
  const { slug } = useLocalSearchParams();

  return (
    <View>
      <Text>Post</Text>
      <Link href="/post/edit">Go back </Link>
    </View>
  );
}
