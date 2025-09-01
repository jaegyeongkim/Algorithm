import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const H = input[0];
const M = input[1];

const whatTime = (H: number, M: number): void => {
  const earlyMinute = H * 60 + M - 45;
  const hour = earlyMinute < 0 ? 23 : Math.floor(earlyMinute / 60);
  const minute = earlyMinute < 0 ? 60 + earlyMinute : earlyMinute % 60;

  console.log(hour, minute);
};

whatTime(H, M);
