/*
Find the Number Occurring Odd Number of Times
Given an array of positive integers. All numbers occur even number of times except one number which occurs odd number of times. Find the number in O(n) time & constant space.

Example:
I/P = [1, 2, 3, 2, 3, 1, 3]
O/P = 3


[A Better Solution] is to use Hashing. Use array elements as key and their counts as value. Create an empty hash table. One by one traverse the given array elements and store counts. Time complexity of this solution is O(n). But it requires extra space for hashing.

Implementing this : 

[The Best Solution] is to do bitwise XOR of all the elements. XOR of all elements gives us odd occurring element. Please note that XOR of two elements is 0 if both elements are same and XOR of a number x with 0 is x.

*/

function findOdd(A) {
	var sum = 0;
	for (var i = 0; i < A.length; i++) {
		sum= sum^A[i];
	}
	if(sum) return sum;
	else return 'No odd occuring element found'
}

console.log(findOdd([1, 2, 3, 2, 3, 1, 3]));
console.log(findOdd([1, 2, 3, 2, 3, 1, 3, 3]));