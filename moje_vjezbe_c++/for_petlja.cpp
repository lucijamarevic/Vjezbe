// C++ program to find the sum of first n natural numbers
// positive integers such as 1,2,3,...n are known as natural numbers

#include <iostream>

using namespace std;

int main() {
    unsigned num, sum; 
    sum = 0;

    cout << "Enter a positive integer: ";
    cin >> num;     // User gives us the number of integers

    for (int count = 1; count <= num; ++count) {     /* For loop starts at one (the first natural number)
                                                    and is continued untill we reach the given number */
        sum += count;
    }

    cout << "Sum = " << sum << endl;

    return 0;
}