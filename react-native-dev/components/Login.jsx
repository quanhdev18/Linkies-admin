import { View, Text, Image, TouchableOpacity } from "react-native";
import React from "react";
import { StyleSheet } from "react-native";
import { useRouter } from "expo-router";

export default function Login() {
  const router = useRouter();

  return (
    <View>
      <Image
        source={require("../assets/images/login.jpg")}
        style={{
          width: "100%",
          height: 500,
        }}
      />
      <View style={styles.container}>
        <Text
          style={{
            fontSize: 30,
            fontFamily: "outfit-bold",
            textAlign: "center",
          }}
        >
          Welcome to Linkies
        </Text>
        <Text
          style={{
            fontSize: 22,
            fontFamily: "outfit-medium",
            textAlign: "center",
            marginTop: 10,
          }}
        >
          Slogan
        </Text>
        <TouchableOpacity
          style={styles.button}
          onPress={() => router.push("auth/sign-in")}
        >
          <Text
            style={{
              textAlign: "center",
              color: "#000",
              fontSize: 20,
              fontFamily: "outfit-medium",
            }}
          >
            Get started
          </Text>
        </TouchableOpacity>
        <Text
          style={{
            textAlign: "center",
            marginTop: 20,
            fontFamily: "outfit",
            fontSize: 16,
            color: "#000",
          }}
        >
          By signing up, you agree to our Term. See how we use your data in our
          Privacy Policy
        </Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: "#fff",
    marginTop: -20,
    borderTopLeftRadius: 30,
    borderTopRightRadius: 30,
    height: "100%",
    padding: 15,
  },
  button: {
    padding: 15,
    backgroundColor: "#fff",
    borderStyle: "solid",
    borderWidth: 2,
    borderColor: "#000",
    marginTop: "25%",
    borderRadius: 99,
  },
});
