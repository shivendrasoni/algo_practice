var G=[[0],[2,3,4],[1,5,6],[1,7],[1,8],[2,9,10],[2],[3,11,12],[4],[5],[5],[7],[7]];

var G_c=[0,0,0,0,0,0,0,0,0,0,0,0];

function DFS(v, target)
{
  var s=[];
  s.push(v);

  while(s.length != 0)
  {
    v=s.pop();
    if (v===target)
    {
      document.write("Found value using DFS , value= "+target+", exiting program now. <br />");
      return 1;
    }
    if(G_c[v]===0)
    {
      G_c[v]=1;
      for (var i = 0; i < G[v].length; i++) {
        s.push(G[v][i]);        
      }
      }
    }

    return 0;

  }
