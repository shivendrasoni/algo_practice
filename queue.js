/* 

Author : Shivendra Soni
version : 1.0
Usage : 

var q=new Queue; // Create a new Queue Object

q.enqueue(item); // Enqueue item to the Queue

var front=q.dequeue(); // Pop item from Front of Queue 

q.isEmpty() ;// Check if Queue is empty

var length =q.getLength(); // get length of Queue

var front=q.peek(); // Get front item from Queue without popping it 

*/



function Queue() {
    var queue = [];
    var offset = 0;

    //Get length of Queue   

    this.getLength = function() {
        return (queue.length - offset);
    }

    // Check if current Queue is Empty
    this.isEmpty = function() {
        return (queue.length == 0);
    }

    // Push element 'item' into the Queue
    this.enqueue = function(item) {
        queue.push(item);
    }

    //Pop and return the front item from from Queue
    this.dequeue = function() {

        if (queue.length == 0) return undefined;

        var item = queue[offset];

        if (++offset * 2 >= queue.length) {
            queue = queue.slice(offset);
            offset = 0;
        }

        return item;
    }

    //Peek at item on the front of Queue without popping it.
    this.peek = function() {
        return (queue.length > 0 ? queue[offset] : undefined);
    }

}
