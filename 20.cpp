#include <iostream>
using namespace std;
typedef unsigned long long ull;
ull fact (size_t i)
{
	ull f = i;
	for (size_t j = 2; j < i; j++)
		f *= j;
	return f;
}
int add (ull num)
{
	int sum = 0;
	while (num > 0)
	{
		sum += (num % 10);
		num /= 10;
	}
	return sum;
}
int main ()
{
    cout << add(fact(100));
    return 0;
}
