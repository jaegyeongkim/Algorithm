import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const a = input[0];

const is윤년 = (input: number): void => {
  if ((input % 4 === 0 && input % 100 !== 0) || input % 400 === 0) {
    console.log(1);
  } else {
    console.log(0);
  }
};

is윤년(a);
