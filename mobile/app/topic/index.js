
import { useLocalSearchParams } from "expo-router";
import { Link } from "expo-router";
import { Text, View } from "react-native";

export default function Topic() {
  const { slug } = useLocalSearchParams();

  return (
    <View>
      <Text>Topic</Text>
      <Link href="/topic/edit">Go back </Link>
    </View>
  );
}
