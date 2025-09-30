// https://www.acmicpc.net/problem/10101

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);
const a1 = input[0];
const a2 = input[1];
const a3 = input[2];
if (a1 + a2 + a3 !== 180) {
  console.log("Error");
} else if (a1 === 60 && a2 === 60 && a3 === 60) {
  console.log("Equilateral");
} else if (a1 === a2 && a2 === a3) {
  console.log("Isosceles");
} else if (a2 === a3 && a3 === a1) {
  console.log("Isosceles");
} else if (a3 === a1 && a1 === a2) {
  console.log("Isosceles");
} else {
  console.log("Scalene");
}
