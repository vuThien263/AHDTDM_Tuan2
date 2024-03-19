#include <stdio.h>
#include <math.h>

int main() {
  int n, count = 0;
  printf("Nhap n: ");
  scanf("%d", &n);

  for (int i = 1; i <= n; i++) {
    if (kiemTraSoChinhPhuong(i)) {
      count++;
      printf("%d ", i);
    }
  }

  printf("\nSo luong so chinh phuong nho hon %d la: %d\n", n, count);
  return 0;
}

int kiemTraSoChinhPhuong(int x) {
  int sqrtX = (int)sqrt(x);
  return sqrtX * sqrtX == x;
}
