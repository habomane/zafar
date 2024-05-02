
import { useLocalSearchParams } from "expo-router";
import { Link } from "expo-router";
import { Text, View } from "react-native";

export default function EditTopicScreen() {
  const { slug } = useLocalSearchParams();

  return (
    <View>
      <Text>Edit Topic</Text>
      <Link href="/">Go back </Link>
    </View>
  );
}
