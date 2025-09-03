// LINK: https://www.acmicpc.net/problem/10811

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

// const input = [5, 4, 1, 2, 3, 4, 1, 4, 2, 2];

const N = input[0];
const M = input[1];
let basket = Array.from({ length: N }, (_: unknown, i: number) => i + 1);
const arr = input.splice(2);

for (let k = 0; k < M; k++) {
  const i = arr[k * 2];
  const j = arr[k * 2 + 1];

  const first = basket.slice(0, i - 1);
  const reverse = basket.slice(i - 1, j).reverse();
  const last = basket.slice(j);

  basket = [...first, ...reverse, ...last];
}
console.log(basket.join(" "));
