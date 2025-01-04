let numbers = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10];

let biggerValue = numbers[0];
for (const val of numbers) {
  if (biggerValue < val) {
    biggerValue = val;
  }
}
console.log(biggerValue);
