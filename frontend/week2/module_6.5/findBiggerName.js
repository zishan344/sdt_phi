var friends = ["rahim", "karim", "abdul", "sadsd", "heroAlom"];
let biggerValue = friends[0];
for (const fnd of friends) {
  if (biggerValue.length < fnd.length) {
    biggerValue = fnd;
  }
}
console.log(biggerValue);
