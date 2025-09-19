// LINK: https://www.acmicpc.net/problem/9506

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

let i = 0;

while (input[i] > 0) {
  let total = 1;
  const arr = [1];
  for (let j = 2; j < input[i]; j++) {
    if (input[i] % j === 0) {
      total += j;
      arr.push(j);
    }
    if (total > input[i]) {
      break;
    }
  }

  if (total === input[i]) {
    console.log(`${input[i]} = ${arr.join(" + ")}`);
  } else {
    console.log(`${input[i]} is NOT perfect.`);
  }
  i++;
}
