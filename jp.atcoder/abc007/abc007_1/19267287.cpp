#include <bits/stdc++.h>
using namespace std;


class Solver {

int n;

void prepare() {
  cin >> n;
}


void solve() {
  cout << n - 1 << '\n';
}


public:

void run() {
  prepare();
  solve();
}

};


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int t = 1;
  while (t--) {
    Solver solver;
    solver.run();
  }

  return 0;
}
