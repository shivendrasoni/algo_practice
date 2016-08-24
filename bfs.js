var G=[[0],[2,3,4],[1,5,6],[1,7],[1,8],[2,9,10],[2],[3,11,12],[4],[5],[5],[7],[7]];


function Queue(){
var queue  = [];
  var offset = 0;

  this.getLength = function(){
    return (queue.length - offset);
  }

  this.isEmpty = function(){
    return (queue.length == 0);
  }

     this.enqueue = function(item){
    queue.push(item);
  }



  this.dequeue = function(){
 
    if (queue.length == 0) return undefined;

    var item = queue[offset];

    if (++ offset * 2 >= queue.length){
      queue  = queue.slice(offset);
      offset = 0;
    }

    return item;
}
this.peek = function(){
    return (queue.length > 0 ? queue[offset] : undefined);
  }

}


function BFS(v, target)
{
	var q= new Queue();
	var V =[];
	q.enqueue(v);

	V.push(v);
	while (!q.isEmpty())
	{
		var t= q.dequeue();

		if (t===target)
			{
				document.write("Found value "+target+", exiting program now.");
				return 1;
			}
			
		for (var u=0; u<G[t].length ; u++)
		{
			if(V.indexOf(G[t][u]) === -1)
			{
				V.push(G[t][u]);
				q.enqueue(G[t][u]);

			}
		}

	}

return 0;
}
