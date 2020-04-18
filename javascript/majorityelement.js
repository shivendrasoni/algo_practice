/*
Majority Element: A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element).

Write a function which takes an array and emits the majority element (if it exists), otherwise prints NONE as follows:

       I/P : 3 3 4 2 4 4 2 4 4
       O/P : 4 

       I/P : 3 3 4 2 4 4 2 4
       O/P : NONE

*/

// Approach chosen : Moores voting algo

function findCandidate(a,size)
{
    var maj_index = 0, count = 1;
    var i;
    for (i = 1; i < size; i++)
    {
        if (a[maj_index] === a[i])
            count++;
        else
            count--;
        if (count === 0)
        {
            maj_index = i;
            count = 1;
        }
    }
    return a[maj_index];
}
 
/* Function to check if the candidate occurs more than n/2 times */
function isMajority(a, size,cand)
{
    var i, count = 0;
    for (i = 0; i < size; i++)
      if (a[i] == cand)
         count++;
    if (count > size/2)
       return 1;
    else
       return 0;
}

function findMajorityElement(arr) {
	var size=arr.length;
	var candidate = findCandidate(arr, size);
	// console.log(candidate);
	if(isMajority(arr, size, candidate)) {
		console.log('majority element is ',candidate);
	}
	else 
		console.log("NONE");
	
}

findMajorityElement([1,2,3,4,32,2,1,2,4,5,6,2,2,2,2,2,2,2,2,2,2,2,2]);
findMajorityElement([1,2,3,3,3,4]);
findMajorityElement([1,2,4]);
