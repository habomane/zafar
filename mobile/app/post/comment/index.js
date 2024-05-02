
import { useLocalSearchParams } from "expo-router";
import { Link } from "expo-router";
import { Text, View } from "react-native";

export default function CommentScreen() {
  const { slug } = useLocalSearchParams();

  return (
    <View>
      <Text>Commenttt</Text>
      <Link href="/post/comment/edit">Go back </Link>
    </View>
  );
}
