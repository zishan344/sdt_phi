#include <bits/stdc++.h>
using namespace std;
int fib(int n)
{
  if (n == 1)
    return 0;
  else if (n == 2)
    return 1;
  return fib(n - 1) + fib(n - 2);
}
int main()
{
  int val;
  cin >> val;
  cout << fib(val);
  return 0;
}
