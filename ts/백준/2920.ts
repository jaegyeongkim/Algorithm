// LINK: https://www.acmicpc.net/problem/2920

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

let isAscending = false;
let isDescending = false;
let isMixed = false;

for (let i = 1; i < 8; i++) {
  if (input[i - 1] < input[i]) {
    isAscending = true;
  } else {
    isDescending = true;
  }
}

if (isAscending && isDescending) {
  console.log("mixed");
} else if (isAscending) {
  console.log("ascending");
} else {
  console.log("descending");
}
