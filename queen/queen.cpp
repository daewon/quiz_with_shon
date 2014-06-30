#include <iostream>

int N = 0;
int used[10000] = {0,};
int queen(int row, int* count) {
  if (row == N) { return (*count)++; }
  for(int col=0; col<N; col++) {
    int c = col, l = row-col+100, r = row+col+1000;
    if (used[c] || used[r] || used[l]) { continue; }

    used[l] = 1; used[c] = 1; used[r] = 1;
    queen(row+1, count);
    used[l] = 0; used[c] = 0; used[r] = 0;
  }
  return 0;
}

int main () {
  int row = 0;
  int times = 0;
  std::cin >> times;

  for(int i=0; i<times; i++) {
    std::cin >> N;
    int count = 0;
    queen(0, &count);
    std::cout << count << std::endl;
  }

  return 0;
}
