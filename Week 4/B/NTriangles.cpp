#include "bits/stdc++.h"
using namespace std;

double pythagorean(double a, double b)
{
    return sqrt(a * a + b * b);
}

double solve(double n, double last, double ratio)
{
    if (n == 0)
        return last;

    double A = last;
    double B = last * ratio;

    // The ratio doesn't change because all the triangles are similar
    return solve(n - 1, pythagorean(A, B), ratio);
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int a, b, n;
    cin >> a >> b >> n;

    // the ratio of the two "legs" of the original triangle
    double ratio = b / a;
    cout << solve(n, pythagorean(a, b), ratio) << "\n";

    return 0;
}