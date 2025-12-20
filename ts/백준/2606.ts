// LINK: https://www.acmicpc.net/problem/2606

import * as fs from "fs";

const input = fs.readFileSync(0, "utf8").split("\n");

const pairCount = Number(input[1]);

const arr = input
  .splice(2, pairCount)
  .map((list) => list.split(" ").map(Number));

const parasitedCom = new Map<number, number[]>();

arr.forEach(([originId, linkedId]) => {
  if (parasitedCom.has(originId)) {
    const existing = parasitedCom.get(originId);
    parasitedCom.set(originId, [...(existing || []), linkedId]);
  } else {
    parasitedCom.set(originId, [linkedId]);
  }

  if (parasitedCom.has(linkedId)) {
    const existing = parasitedCom.get(linkedId);
    parasitedCom.set(linkedId, [...(existing || []), originId]);
  } else {
    parasitedCom.set(linkedId, [originId]);
  }
});

const parasitedComList = [1];

let idx = 0;
while (1) {
  const num = parasitedComList[idx];
  const newParasitedList = parasitedCom.get(num);

  newParasitedList?.length &&
    newParasitedList.forEach((com) => {
      if (!parasitedComList.includes(com)) {
        parasitedComList.push(com);
      }
    });

  idx++;
  if (idx >= parasitedComList.length) break;
}

console.log(parasitedComList.length - 1);
