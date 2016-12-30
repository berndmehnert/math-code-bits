/* (C) by B. Mehnert (nickname bhmehnert) under the license presented in this directory.
 *
 * This program computes a vector of the primes smaller or equal to a given integer n.
 * The algorithm used is the 'Sieve of Eratosthenes', which is a quite fast algorithm.
 * Our choice of data structure is a doubly linked list. */

#include <iostream>
#include <cmath>  // I need this for computing the square root of a number. 
#include <vector>

using namespace std;

typedef struct DLLNode
{
	DLLNode *lNode;
	DLLNode *rNode;
	int Data;
}DLLNode;

/* Function 'primes':
 * Input: An integer n => 2.
 * Output: A vector containing all primes p <=n */

vector<int>  primes(int n)
{
	// First we initialize the list where we cross out the non-primes.
	
	DLLNode *List = new DLLNode [n-1];
	
	// Store the n-1 numbers 2,3,4,5,...,n in the doubly linked list List[0] <-> List[1] <-> .. <-> List[n-2].

	for (int i=0; i < n-1; i++)
	{
		if (i > 0) List[i].lNode = &List[i-1];
	    if (i < n-2) List[i].rNode = &List[i+1];
	    List[i].Data = i+2;
	};

	int t = (int) sqrt((float) n);  // Any non-prime <= n has a prime divisor <= t = [sqrt(n)]. 
	
	DLLNode *first = &List[0];
	DLLNode *pos = &List[0];
	DLLNode *run = &List[0];

	// Now follows the main algorithm. Note that the integer d is always a prime, beginning with d=2.
	
	int d = pos -> Data;
	
	while (d <= t) 
	{
		// Go through all numbers to the right of pos which are not crossed out yet
		// and cross those out which are multiples of d. 

		while (run -> rNode != NULL)
		{
			run = run -> rNode;
			if ((run -> Data) % d == 0)
			{
				if (run -> rNode != NULL) 
				{
					(run -> lNode) -> rNode = run -> rNode;
					(run -> rNode) -> lNode = run -> lNode;
				}
				else
				{
					(run -> lNode) -> rNode = NULL;
				};
			};
		};
		pos = pos -> rNode; 
		run = pos;
		d = pos -> Data;
	};

	run = first;
	int counter = 0;
	vector<int> output;

	while (run != NULL) 
	{
		output.push_back(run -> Data);
		run = run -> rNode;
	};

	// Free the memory of the list we used:
	delete [] List;

	return output;
}



int main()
{
	// Let's compute a list of the prime numbers p with 2 <= p <= 1000000
	// and print them out.
	
	vector<int> v = primes(1000000);
	
    for (int i=0; i < v.size(); i++)
	{
		cout << v[i] << ", ";
	};

	return 0;
}
