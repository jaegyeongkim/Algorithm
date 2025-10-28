// LINK: https://www.acmicpc.net/problem/1181

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(String);

const arr = new Set(
  input.splice(1).sort((a, b) => {
    if (a.length !== b.length) {
      return a.length - b.length;
    }

    return a.localeCompare(b);
  })
);

arr.forEach((str) => {
  console.log(str);
});
