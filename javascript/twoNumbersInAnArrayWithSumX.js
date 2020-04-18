/*Write a C program that, given an array A[] of n numbers 
and another number x, determines whether or not there exist
 two elements in A whose sum is exactly x. */

 /*Approach 1: 

1) sort array A

2) iterate through A[0] to A[A.length-2]
	3) for every A[i], find x-A[i] in A[i+1 to length-1];
		if found (return A[i], x-A[i])
	return 0;


approach 2 : 
1) Sort the array in non-decreasing order.
2) Initialize two index variables to find the candidate 
   elements in the sorted array.
       (a) Initialize first to the leftmost index: l = 0
       (b) Initialize second  the rightmost index:  r = ar_size-1
3) Loop while l < r.
       (a) If (A[l] + A[r] == sum)  then return 1
       (b) Else if( A[l] + A[r] <  sum )  then l++
       (c) Else r--    
4) No candidates in whole array - return 0
 */

 var binarySearch = function (arr, l, r ,x) {
 	// console.log(l,r)
 	if(r>=l)
 	{
 		var mid = parseInt((l+r)/2);
		// console.log(arr[l],arr[mid],arr[r],x);
 		if(arr[mid]===x) {
 			console.log("found")
 			return true;
 		}

 		else if(x<arr[mid]) {
 			// console.log('left');
 			return binarySearch(arr, l, mid-1, x);
 		}
 		else {
 			// console.log('right');
 			return binarySearch(arr, mid+1, r, x);
 		}
 	}
 	return false;
 }

 var findNumbers_1 = function (A, x) {

 	A.sort(function (a,b) {
 		return a-b;
 	});
 	
 	var len = A.length;
 	
 	for(var i =0; i<len-1; i++) {
 		if(binarySearch(A, i+1, len-1, x-A[i])) {

 			return 1;
 		}
 	}

 	return 0;
 }


var findNumbers_2 = function(A, x) {
	var len = A.length;

    /* Sort the elements */
    A.sort(function (a,b) {
    	return a-b;
    });

    
     
    /* Now look for the two candidates in the sorted 
       array*/
    var l = 0;
    var r = len-1; 
    while (l < r)
    {
         if(A[l] + A[r] == x)
              return 1; 
         else if(A[l] + A[r] < x)
              l++;
         else // A[i] + A[j] > x
              r--;
    }    
    return 0;

}
console.log("result with approach 1 : "+findNumbers_1([1, 4, 45, 6, 10, -8], 16));

console.log("result with approach 2 :"+findNumbers_2([1, 4, 45, 6, 10, -8], 16));







