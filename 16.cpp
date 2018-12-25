#include<iostream>
#include<math.h>
using namespace std;
int main()
{
	auto n = 200;
	auto x = n * (log(2) / log(10));
	auto num = pow(10, x);
	auto sum = 1;
	cout << num << endl;
	while(num > 0)
	{
		cout << "sum = " << sum << " (n % 10) = " << ((unsigned long long)num % (unsigned long long)10) << endl;
		sum += ((unsigned long long)num % (unsigned long long)10);
		num /= 10;
		num = (unsigned long long)num;
	}
	cout << sum;
	return 0;
}