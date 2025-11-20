// LINK: https://www.acmicpc.net/problem/10845

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split("\n").map(String);

const N = Number(input[0]);
const queue: any[] = [];
const result: any[] = [];

for (let i = 1; i < N + 1; i++) {
  switch (input[i]) {
    case "pop":
      if (queue.length) {
        result.push(queue.shift());
      } else {
        result.push(-1);
      }
      break;
    case "size":
      result.push(queue.length);
      break;
    case "empty":
      result.push(queue.length ? 0 : 1);
      break;
    case "front":
      if (queue.length) {
        result.push(queue[0]);
      } else {
        result.push(-1);
      }
      break;
    case "back":
      if (queue.length) {
        result.push(queue[queue.length - 1]);
      } else {
        result.push(-1);
      }
      break;
    default:
      const [_, X] = input[i].split(" ");
      queue.push(X);
      break;
  }
}

process.stdout.write(result.join("\n").replace(/,/g, " "));
