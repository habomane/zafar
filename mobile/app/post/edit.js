
import { useLocalSearchParams } from "expo-router";
import { Link } from "expo-router";
import { Text, View } from "react-native";

export default function EditPost() {
  const { slug } = useLocalSearchParams();

  return (
    <View>
      <Text>Post Edit</Text>
      <Link href="/post/comment/"> post edit </Link>
    </View>
  );
}
