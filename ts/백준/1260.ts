// LINK: https://www.acmicpc.net/problem/1260

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split("\n").map(String);

const [N, M, V] = input[0].split(" ").map(Number);
const arr = input.splice(1, M);

const dfsMap = Array.from({ length: N + 1 }, () => new Array(N + 1).fill(0));
const bfsMap = Array.from({ length: N + 1 }, () => new Array(N + 1).fill(0));

arr.forEach((unit) => {
  const [r, c] = unit.split(" ").map(Number);
  dfsMap[r][c] = 1;
  dfsMap[c][r] = 1;
  bfsMap[r][c] = 1;
  bfsMap[c][r] = 1;
});

const dfs = [V];
const dfsAnswer: number[] = [];
const dfsVisited = new Array(N + 1).fill(0);

while (dfs.length) {
  const cur = dfs.pop() as number;
  if (dfsVisited[cur]) continue;
  dfsVisited[cur] = 1;
  dfsAnswer.push(cur);

  for (let next = N; next > 0; next--) {
    if (dfsMap[cur][next] === 1 && !dfsVisited[next]) {
      dfs.push(next);
    }
  }
}

const bfs = [V];
const bfsAnswer: number[] = [];
const bfsVisited = new Array(N + 1).fill(0);

while (bfs.length) {
  const cur = bfs.shift() as number;

  if (bfsVisited[cur]) continue;
  bfsVisited[cur] = 1;
  bfsAnswer.push(cur);

  for (let next = 1; next <= N; next++) {
    if (bfsMap[cur][next] === 1 && !bfsVisited[next]) {
      bfs.push(next);
    }
  }
}

console.log(dfsAnswer.join(" "));
console.log(bfsAnswer.join(" "));
