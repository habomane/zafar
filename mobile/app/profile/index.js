import { useLocalSearchParams } from "expo-router";
import { Link } from "expo-router";
import { Text, View } from "react-native";

export default function ProfileIndex() {
  const { slug } = useLocalSearchParams();

  return (
    <View>
      <Text>On the profile this one</Text>
      <Link href="/profile/edit">Go back </Link>
    </View>
  );
}
