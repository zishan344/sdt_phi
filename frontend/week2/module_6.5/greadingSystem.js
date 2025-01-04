let number = 60;

let grade;

if (number >= 0 && number <= 39) {
  grade = "C";
} else if (number >= 40 && number <= 59) {
  grade = "B";
} else if (number >= 60 && number <= 69) {
  grade = "A-";
} else if (number >= 70 && number <= 79) {
  grade = "A";
} else if (number >= 80 && number <= 100) {
  grade = "A+";
} else {
  grade = "Invalid";
}

console.log(`Your grade is: ${grade}`);
