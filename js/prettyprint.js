
	//param A : integer
	//return a array of array of integers

    /*
        if A = 4
        return 
        
        4 4 4 4 4 4 4
        4 3 3 3 3 3 4
        4 3 2 2 2 3 4
        4 3 2 1 2 3 4
        4 3 2 2 2 3 4
        4 3 3 3 3 3 4
        4 4 4 4 4 4 4 
    */
	var prettyPrint = function(A){
	    var matrix = [];

        if(A===1) return [[1]];
	    
	    for(var j = 0; j < 2*A-1; j++ ) {
	        matrix[j] = new Array(2*A-1);
            matrix[j].fill(0);
	    }
    
    
    function printBoundry(x) {
        // break condition 
        if(x > A) {
            return ;
        }
        
        if(x ===1) {
            matrix[A][A] = 1;
        }
        var lb = A-x,rb = A+x-2, tb =A-x, bb = A+x-2;
        var i;
        for(i = lb; i<=rb; i++) {
            matrix[tb][i]=x;
            matrix[bb][i] =x;
        }
        tb++; bb--;
        for(i=tb; i<=bb;i++) {
            matrix[i][rb]=x;
            matrix[i][lb]=x;
        } 
        printBoundry(x+1);
    }
    printBoundry(1);
    return matrix;
	}

console.log(prettyPrint(1));