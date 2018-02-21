#include <iostream>
using namespace std;
#include <cmath>
// 512 = 2^4 * 3^4 * 5^4 * 7 * 11
auto isTriangle(auto n)
{
	auto temp = floor(sqrt(2 * n));
	return n == (temp * (temp + 1) / 2);
}
auto lastTerm(auto n)
{
	if(isTriangle(n))
		return floor(sqrt(2 * n));
	return 0;
}
auto divisor(int n)
{
	auto count = 2;
	for(auto i = 2; i < double(floor(pow(n, 0.5))) + 1; i++)
		if(n % i == 0)
		{		
			count++;
			if(i != (n / i))
				count++;
		}
	return count;
		
}
int main()
{
	auto check = (pow(2,4)) * (pow(3,4)) * (pow(5,4)) * (7) * (11);
	while(!isTriangle(check))
		check++;
	auto lastT = lastTerm(check);
	while(divisor(check) < 500)
	{
		check += (lastT + 1);
		lastT++;
	}
	cout << (unsigned long long)(check);
	return 0;
}