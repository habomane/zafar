
import { useLocalSearchParams } from 'expo-router';
import { Link } from 'expo-router';
import { Text, View } from 'react-native';

export default function PageTwo() {
  const { slug } = useLocalSearchParams();

  return (<View><Text>Second Page</Text><Link href="/profile">Go back </Link></View>);
}
