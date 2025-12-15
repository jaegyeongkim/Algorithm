// LINK: https://www.acmicpc.net/problem/17219

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").split("\n");

const [N, M] = input[0].split(" ").map(Number);
const arr = input.splice(1);

const test = new Map();
for (let i = 0; i < N; i++) {
  const [address, password] = arr[i].split(" ").map(String);

  test.set(address, password);
}

for (let i = N; i < N + M; i++) {
  const [address] = arr[i].split(" ");

  console.log(test.get(address));
}
