#include <iostream>

int gcd(int a, int b) {
    if (b==0) { return a; } else return gcd(b, a % b);
}

int main() {

    int count = 0;

    for (auto d = 2; d <= 12000; d++) {
        for (auto n = (d+1)/3; n <= (d+1)/2; ++n) {
            if (gcd (n, d) == 1) { count ++; }
        }
    }

    std::cout << count << std::endl;

    return 0;
}
