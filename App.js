import React, { useState } from "react";

import {
  StyleSheet,
  Text,
  View,
  Button,
  TextInput,
  ScrollView,
} from "react-native";

import songList from "./assets/finishedSanitized.json";

export default function App() {
  const [text, onChangeText] = useState("");
  const [output, setOutput] = useState([]);

  const handleOnClick = () => {
    let search = text.toLowerCase().split("").sort().join("");

    for (var i in songList) {
      var word = songList[i].split("").sort().join("");

      if (search === word) {
        console.log(songList[i]);
        setOutput([...output, songList[i]]);
      }
    }
  };

  return (
    <View style={styles.container}>
      <Text>Enter anagram</Text>
      <TextInput
        style={styles.input}
        onChangeText={onChangeText}
        value={text}
      />
      <Button title="Søk" onPress={handleOnClick} />
      {output && output.map((val, index) => <Text key={index}>{val}</Text>)}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
  input: {
    height: 40,
    margin: 12,
    borderWidth: 1,
    padding: 10,
  },
});
