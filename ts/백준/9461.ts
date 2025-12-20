// LINK: https://www.acmicpc.net/problem/9461

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const N = input[0];
const arr = input.splice(1);

const triangles = [1, 1, 1, 2, 2];

for (let num of arr) {
  while (triangles.length < num) {
    triangles.push(
      triangles[triangles.length - 1] + triangles[triangles.length - 5]
    );
  }
  console.log(triangles[num - 1]);
}
