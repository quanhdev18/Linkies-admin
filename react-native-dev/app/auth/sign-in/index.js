import {
  View,
  Text,
  StyleSheet,
  TextInput,
  TouchableOpacity,
} from "react-native";
import React, { useEffect } from "react";
import { useNavigation, useRouter } from "expo-router";
import { Ionicons } from "@expo/vector-icons";

export default function SignIn() {
  const router = useRouter();
  const navigation = useNavigation();

  useEffect(() => {
    navigation.setOptions({
      headerShown: false,
    });
  });

  return (
    <View
      style={{
        padding: 25,
        paddingTop: 40,
        height: "100%",
      }}
    >
      <TouchableOpacity onPress={() => router.back()}>
        <Ionicons name="arrow-back" size={24} color="black" />
      </TouchableOpacity>
      <Text
        style={{
          fontSize: 30,
          fontFamily: "outfit-bold",
          marginTop: 30,
        }}
      >
        Let's Sign You In
      </Text>
      <Text
        style={{
          marginTop: 20,
          fontFamily: "outfit",
          fontSize: 24,
        }}
      >
        We only use phone numbers to make sure everyone on Linkies is real.
      </Text>
      {/* phone number */}
      <View
        style={{
          marginTop: 50,
        }}
      >
        <Text
          style={{
            fontFamily: "outfit",
            fontSize: 16,
          }}
        >
          Phone number
        </Text>
        <TextInput
          style={styles.input}
          placeholder="Enter phone number"
          keyboardType="number-pad"
          maxLength={10}
        />
      </View>
      {/* password */}
      <View
        style={{
          marginTop: 30,
        }}
      >
        <Text
          style={{
            fontFamily: "outfit",
            fontSize: 16,
          }}
        >
          Password
        </Text>
        <TextInput
          style={styles.input}
          placeholder="Enter password"
          secureTextEntry={true}
        />
      </View>

      {/* Sign In button */}
      <View
        style={{
          padding: 20,
          backgroundColor: "#000",
          borderRadius: 15,
          marginTop: 50,
        }}
      >
        <Text
          style={{
            color: "#fff",
            textAlign: "center",
          }}
        >
          Sign In
        </Text>
      </View>

      {/* create account button */}
      <TouchableOpacity
        style={{
          padding: 20,
          borderRadius: 15,
          marginTop: 20,
          borderWidth: 1,
        }}
        onPress={() => router.replace("auth/sign-up")}
      >
        <Text
          style={{
            color: "#000",
            textAlign: "center",
          }}
        >
          Create account
        </Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  input: {
    padding: 15,
    borderWidth: 1,
    borderRadius: 15,
    borderColor: "#ccc",
    marginTop: 10,
  },
});
