#include <iostream>

int main() {

    int max_a = 2, max_b = 5;
    for (int b = 2; b <= 1000000; b++) {
        int a = 3*b / 7;
        if (max_a*b < a*max_b && 3*b != 7*a) {
            max_a = a;
            max_b = b;
        }
    }

    std::cout << max_a << std::endl;
    return 0;
}
