#include <iostream>
using namespace std;
int main()
{
    short DAYS[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    size_t c = 0;
    size_t sum = 3;
    for (size_t k = 1901; k <= 2000; k++)
    {
        size_t N = k;
        bool leap = false;
        if (N % 400 == 0)
            leap = true;
        else if (N % 100 != 0 && N % 4 == 0)
            leap = true;
        if (leap)
            DAYS[1] = 29;
        else
            DAYS[1] = 28;
        for (size_t i = 0; i < 12; i++)
        {
            if (sum == 1)
                c++;
            sum += DAYS[i] % 7;
            sum %= 7;
        }
    }
    cout << c << endl;
    return 0;
}
