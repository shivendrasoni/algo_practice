//Generate all prime numbers till n

function f(n){
	// var n = 5;

	var arr = new Array(n);

	var prime = new Array(n+1).fill(true);

	prime[0] = false; prime[1] = false;

	for (var p=2; p*p<=n; p++)
	{
	    // If prime[p] is not changed, then it is a prime
	    if (prime[p] == true)
	    {
	        // Update all multiples of p
	        for (var i=p*2; i<=n; i += p)
	            prime[i] = false;
	    }
	}
}

console.log(f(5));