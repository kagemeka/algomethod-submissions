#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m; cin >> n >> m;
  int t = (1900 * m + 100 * (n - m)) * pow(2, m);
  cout << t << '\n';
  return 0;
}
