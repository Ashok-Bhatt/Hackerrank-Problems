#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    
    int a;
    long b;
    char c;
    float d;
    double e;
    
    cin >> a >> b >> c >> d >> e;
    
    cout << a << endl;
    cout << b << endl;
    cout << c << endl;
    printf("%.3f\n",d);
    printf("%.9lf\n",e);
    
    return 0;
}