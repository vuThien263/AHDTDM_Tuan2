#include <stdio.h>

int main() {
  int i;
  for (i = 1; i <= 99; i++) {
    if (i % 7 == 0) {
      printf("%d ", i);
    }
  }
  printf("\n");
  return 0;
}
