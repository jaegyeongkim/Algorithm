// LINK: https://www.acmicpc.net/problem/1260

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split("\n").map(String);

const [N, M, V] = input[0].split(" ").map(Number);
const arr = input.splice(1, M);

const dfsMap: number[][] = Array.from({ length: N + 1 }, () =>
  new Array(N + 1).fill(0)
);

const bfsMap: number[][] = Array.from({ length: N + 1 }, () =>
  new Array(N + 1).fill(0)
);

arr.forEach((unit) => {
  const [x, y] = unit.split(" ").map(Number);
  dfsMap[x][y] = 1;
  dfsMap[y][x] = 1;
  bfsMap[x][y] = 1;
  bfsMap[y][x] = 1;
});

const dfsIdx = dfsMap[V].findIndex((v) => v === 1);
const dfs = [[V, dfsIdx]];
const dfsResult = [V, dfsIdx];

while (dfs) {
  const [x, y] = dfs.pop() as number[];

  dfsMap[x][y] = 0;
  dfsMap[y][x] = 0;

  const idx = dfsMap[y].findIndex((v) => v === 1);
  if (idx === -1) {
    break;
  }

  dfs.push([y, idx]);
  if (!dfsResult.includes(y)) {
    dfsResult.push(y);
  }
}

const bfsIdx = bfsMap[V].findIndex((v) => v === 1);
const bfs = [[V, bfsIdx]];
const bfsResult = [V, bfsIdx];

while (bfs) {
  const [x, y] = bfs.shift() as number[];

  bfsMap[x][y] = 0;
  bfsMap[y][x] = 0;

  bfsMap[x].filter((v, idx) => {
    if (v === 1) {
      bfs.push([x, idx]);
      bfsMap[x][idx] = 0;
      bfsMap[idx][x] = 0;
    }
  });

  bfsMap[y].filter((v, idx) => {
    if (v === 1) {
      bfs.push([y, idx]);
      bfsMap[y][idx] = 0;
      bfsMap[idx][y] = 0;
    }
  });

  if (!bfsResult.includes(y)) {
    bfsResult.push(y);
  }

  if (bfs.length === 0) break;
}

console.log(dfsResult.join(" "));
console.log(bfsResult.join(" "));
