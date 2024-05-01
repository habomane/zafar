
import { useLocalSearchParams } from "expo-router";
import { Link } from "expo-router";
import { Text, View } from "react-native";

export default function Profile() {
  const { slug } = useLocalSearchParams();

  return (
    <View>
      <Text>Edit the profile</Text>
      <Link href="/post">Go back </Link>
    </View>
  );
}
