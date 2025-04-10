import { Ionicons } from '@expo/vector-icons';
import MaterialCommunityIcons from '@expo/vector-icons/MaterialCommunityIcons';
import { Stack, Tabs } from "expo-router";
import './globals.css';
import { useFonts } from 'expo-font';
export default function RootLayout() {

    useFonts({
        'outfit': require('../assets/fonts/Outfit-Regular.ttf'),
        'outfit-bold': require('../assets/fonts/Outfit-Bold.ttf'),  
        'outfit-medium': require('../assets/fonts/Outfit-Medium.ttf'),
    })

    return (
        <Stack>
            <Stack.Screen name='index' options={{
                headerShown: false
            }} />
        </Stack>
    );
}