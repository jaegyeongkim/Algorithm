// LINK: https://www.acmicpc.net/problem/1966

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split("\n");

const cnt = Number(input[0]);
const arr = input.splice(1);

for (let i = 0; i < cnt * 2; i += 2) {
  const [N, M] = arr[i].split(" ").map(Number);
  const origin = arr[i + 1].split(" ").map(Number);
  let list = origin.map((num, idx) => [idx, num]);

  const sorted = origin.sort((a, b) => b - a);

  let result = 0;
  let isDone = false;
  for (const num of sorted) {
    if (isDone) break;

    while (1) {
      if (isDone) break;
      const n = list[0][0];
      const m = list[0][1];

      if (m === num) {
        list = list.splice(1);
        result++;
        if (n === M) {
          isDone = true;
        }
        break;
      } else {
        const left = list.shift()!;
        list.push(left);
      }
    }
  }

  console.log(result);
}
