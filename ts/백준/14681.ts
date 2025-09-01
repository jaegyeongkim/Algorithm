// LINK: https://www.acmicpc.net/problem/14681

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const x = input[0];
const y = input[1];

const whatYourSquare = (x: number, y: number): void => {
  if (x > 0 && y > 0) {
    console.log(1);
  } else if (x < 0 && y > 0) {
    console.log(2);
  } else if (x < 0 && y < 0) {
    console.log(3);
  } else if (x > 0 && y < 0) {
    console.log(4);
  }
};

whatYourSquare(x, y);
