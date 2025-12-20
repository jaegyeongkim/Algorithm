// LINK: https://www.acmicpc.net/problem/1764

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").trim().split("\n").map(String);
const [N] = input[0].split(" ").map(Number);

const arr = input.splice(1);

const listenX = arr.splice(0, N);
const watchX = arr;

const setListen = new Set(listenX);
const setWatch = new Set(watchX);

const result: string[] = [];
setWatch.forEach((watch) => {
  setListen.has(watch) && result.push(watch);
});

console.log(result.length);
console.log(result.sort((a, b) => a.localeCompare(b)).join("\n"));
