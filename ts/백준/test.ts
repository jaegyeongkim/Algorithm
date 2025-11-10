// console.log("call");

// setTimeout(() => console.log(1));
// setTimeout(() => console.log(2), 0);
// setTimeout(() => console.log(3), 10);

// const setInterval1 = setInterval(() => {
//   console.log(4);
//   clearInterval(setInterval1);
// });
// const setInterval2 = setInterval(() => {
//   console.log(5);
//   clearInterval(setInterval2);
// }, 0);
// const setInterval3 = setInterval(() => {
//   console.log(6);
//   clearInterval(setInterval3);
// }, 10);

// setImmediate(() => console.log(7));
// setImmediate(() => console.log(8));
// setImmediate(() => console.log(9));

// console.log("=== 1. Top-level (메인 모듈) 실행 ===");
// setTimeout(() => console.log("timeout"), 0);
// setImmediate(() => console.log("immediate"));

// console.log("\n=== 2. I/O 콜백 안에서 실행 ===");
// const fs = require("fs");

// // 파일 읽기 I/O 콜백 안에서 실행
// fs.readFile(__filename, () => {
//   console.log("I/O 콜백 시작");
//   setTimeout(() => console.log("timeout in I/O"), 0);
//   setImmediate(() => console.log("immediate in I/O"));
//   console.log("I/O 콜백 끝");
// });

// 또는 다른 방법으로 I/O 콜백 만들기
setTimeout(() => {
  console.log("\n=== 3. Timer 콜백 안에서 실행 ===");
  setTimeout(() => console.log("timeout in timer"), 0);
  setImmediate(() => console.log("immediate in timer"));
}, 100);
