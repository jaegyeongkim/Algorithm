// https://www.acmicpc.net/problem/15894
import fs from "fs";

const input = Number(fs.readFileSync(0, "utf8").trim().split(/\s+/));

console.log(input * 4);
