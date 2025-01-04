function monthlySavings(allPayments, livingCost) {
  if (!Array.isArray(allPayments) || typeof livingCost !== "number") {
    return "invalid input";
  }

  let totalPayments = 0;
  for (const payment of allPayments) {
    if (typeof payment != "number") {
      return "invalid input";
    }
    if (payment >= 3000) {
      let tax = (payment / 100) * 20;
      totalPayments += payment - tax;
    } else totalPayments += payment;
  }

  const savings = totalPayments - livingCost;

  if (savings >= 0) {
    return savings;
  } else {
    return "earn more";
  }
}

console.log(monthlySavings([1000, 2000, 3000], 5400));
console.log(monthlySavings([1000, 2000, 2500], 5000));
console.log(monthlySavings([900, 2700, 3400], 10000));
console.log(monthlySavings([100, [900, 2700], 3400], 5000));
