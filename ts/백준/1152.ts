// LINK: https://www.acmicpc.net/problem/1152

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8");
// const input = "The Curious Case of Benjamin Button";
// const input = " The first character is a blank";
// const input = "The last character is a blank ";
// const input = "         ";

const countLetter = (str: string): number => {
  const letter = str.trim().split(/\s+/).map(String);

  if (letter[0] === "") return 0;
  return letter.length;
};

console.log(countLetter(input));
