/*
	Use euclidean algo to find gcd of two numbers
*/

var gcd = function(A, B){
	    var max = Math.max(A,B);
	    var min = Math.min(A,B);
	    
	    while(min!=0) {
	        var t = min;
	        min = max % min;
	        max =t;
	    }
	    
	    return max;

	}

console.log(gcd(18,6));