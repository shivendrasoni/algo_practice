var isPrime= function(A){
	    if(A==0 || A==1) return 0;
	    if(A==2) return 1;
	    
	    var n = Math.sqrt(A);
	    var i =2;
	    while(i<=n) {
	        if(A%i==0) {
	        	return 0
	        };
	        i++;
	    }
	    
	    return 1;

	}

	console.log(isPrime(39601));