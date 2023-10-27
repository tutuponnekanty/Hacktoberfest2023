/*The Collatz conjecture is one of the most famous unsolved problems in mathematics.
The conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1.
It concerns sequences of integers in which each term is obtained from the previous term as follows:
if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1.
The conjecture is that these sequences always reach 1, no matter which positive integer is chosen to start the sequence.

It is named after the mathematician Lothar Collatz, who introduced the idea in 1937, two years after receiving his doctorate.
It is also known as the 3n + 1 problem (or conjecture), the 3x + 1 problem (or conjecture), the Ulam conjecture (after Stanisław Ulam),
Kakutani's problem (after Shizuo Kakutani), the Thwaites conjecture (after Sir Bryan Thwaites), Hasse's algorithm (after Helmut Hasse),
or the Syracuse problem.

The sequence of numbers involved is sometimes referred to as the hailstone sequence,
hailstone numbers or hailstone numerals (because the values are usually subject to multiple descents and ascents like hailstones in a cloud), or as wondrous numbers.
*/


#include <iostream>
using namespace std;

// Function to calculate the next number in the Collatz sequence
int collatz(int n) {
    if (n % 2 == 0) {
        return n / 2; // If n is even, return n divided by 2
    } else {
        return 3 * n + 1; // If n is odd, return 3n + 1
    }
}

// Function to print the Collatz sequence for a given starting number
void collatzSequence(int n) {
    while (n != 1) {
        cout << n << " -> "; // Print the current number in the sequence
        n = collatz(n); // Calculate the next number using the collatz function
    }
    cout << "1" << endl; // Print the final 1 in the sequence
}

int main() {
    int startNumber;

    // Get user input for the starting number
    cout << "Enter a positive integer to start the Collatz sequence: ";
    cin >> startNumber;

    if (startNumber <= 0) {
        cout << "Please enter a positive integer." << endl;
        return 1; // Exit with an error code if a non-positive integer is entered
    }

    collatzSequence(startNumber); // Call the function to print the Collatz sequence

    return 0; // Exit with a success code
}
