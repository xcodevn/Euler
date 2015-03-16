#include <iostream>
#include <vector>

const long long int MAX = 1000000;

int main() {
    std::vector<int> p(MAX+1, 0);
    std::vector<int> phi(MAX+1, 1);

    long long int sum = 0;
    
    for (long long int i = 2; i <= MAX; ++i) {
        if (p.at(i) == 0) {
            phi.at(i) = i - 1;
            for (auto j = i; j*i <= MAX; ++j) { p.at(i*j) = i; }
        } else {
            auto m = p.at(i);
            auto n = i / m;
            auto d = ( (n % m == 0) ? m : 1 );
            phi.at(i) = phi.at(m) * phi.at(n) * d / phi.at(d);
        }
        sum += phi.at(i);
    }

    std::cout << sum << std::endl;

    return 0;
}
