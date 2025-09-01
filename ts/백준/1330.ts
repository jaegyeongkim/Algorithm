import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const a = input[0];
const b = input[1];

const whatIsBig = (a: number, b: number): void => {
  if (a > b) {
    console.log(">");
  } else if (a === b) {
    console.log("==");
  } else {
    console.log("<");
  }
};

whatIsBig(a, b);
