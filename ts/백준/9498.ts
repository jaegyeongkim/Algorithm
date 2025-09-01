import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const point = input[0];

const whatYourGrade = (point: number): void => {
  if (point >= 90) {
    console.log("A");
  } else if (point >= 80) {
    console.log("B");
  } else if (point >= 70) {
    console.log("C");
  } else if (point >= 60) {
    console.log("D");
  } else {
    console.log("F");
  }
};

whatYourGrade(point);
