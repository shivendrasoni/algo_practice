//generate binary representation of a non negative integer

var f = function(A){
	    var res =  [];
	    
	    if(A===0) return 0;
	    while(A>0) {
	        res.unshift(A%2);
	        A = parseInt(A/2);
	    }
	    
	    return res.join("");
	    
	    
	 
	}

	console.log(f(6));