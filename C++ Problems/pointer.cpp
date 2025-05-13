#include <stdio.h>
#include <algorithm>
using namespace std;

void update(int *a,int *b) {
    if (*a<*b)
        swap(*a,*b);
    *a = *a + *b;
    *b = *a - *b - *b;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
