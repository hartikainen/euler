#include <stdio.h>
#include <map>


unsigned long long printed[7];

int ackermann(std::map<std::pair<int, int>, int> A, unsigned long long m, unsigned long long n) {
  int result;

// std::map<std::pair<int,int>, int> myMap;

// myMap[std::make_pair(10,20)] = 25;
// std::cout << myMap[std::make_pair(10,20)] << std::endl;

  // if (A.find(std::make_pair(m, n)) != A.end()) {
  //   return A[std::make_pair(m, n)];
  // }

  if (m == 0) {
    result = n+1U;
  } else if (m == 1) {
    result = n+2U;
  } else if (n == 0) {
    result = ackermann(A, m-1LLU, 1LLU);
  } else {
    result = ackermann(A, m-1LLU, ackermann(A, m, n-1U));
  }

  // A[std::make_pair(m, n)] = result;

  if (m == n && !printed[m]) {
    printf("A(%llu, %llu) == %d\n", m, n, result);
    printed[m] = 1;
  }

  return result;
}

int main() {
  std::map<std::pair<int,int>, int> A;
  printf("jiiri");
  ackermann(A, 4LLU, 4LLU);

  // for (int i=0; i<7; i++) {
  //   for (int j=0; j<7; j++) {
  //     printf("i: %d, j: %d", i, j);
  //     ackermann(A, i, j);
  //   }
  // }

  // for (int i=0; i<7; i++) {
  //   printf("ackermann(%d,%d) == ", i, i);
  //   printf("%d\n", ackermann(A, i, i));
  //   // for (int m=0; m<i; m++) {
  //   //   printf("\n");
  //   //   for (int n=0; n<i; n++) {
  //   //     printf("%d", A[std::make_pair(m, n)]);
  //   //   }
  //   // }
  // }
  return -1;
}
