Function Node(data) {
	this.next = null;
	this.data = data;
}


Function SinglyList() {
this.length = 0;
this.head = null;
}

var list1 = new SinglyList();

SinglyList.prototype  = {
	constructor : SinglyList,
	addNode : function(data) {
		var node = new Node(data);
		var currentNode = this.head;

		if(!currentNode) {
			this.head = node; 
			this.length++;
			return node;
		}

		while(currentNode->next) {
			currentNode = currentNode.next;
		}
		currentNode.next = node;
		this.length++;
		return node;
	},
	getNodeAtPosition: function (position) {
		var currentNode = this.head,
		length = this.length,
		count=1;

		if(length ===0 || position > length || position < 1) {
			throw new Error("node can not be found in this position in list.")
		}

		while(count < position) {
			currentNode = currentNode.next;
			count++;
		}
		return currentNode;
	},
	removeNode : function (position) {
		var currentNode = this.head,
	        length = this._length,
	        count = 0,
	        message = {failure: 'Failure: non-existent node in this list.'},
	        beforeNodeToDelete = null,
	        nodeToDelete = null,
	        deletedNode = null;
	 
	    // 1st use-case: an invalid position
	    if (position < 0 || position > length) {
	        throw new Error(message.failure);
	    }
	 
	    // 2nd use-case: the first node is removed
	    if (position === 1) {
	        this.head = currentNode.next;
	        deletedNode = currentNode;
	        currentNode = null;
	        this._length--;
	         
	        return deletedNode;
	    }
	 
	    // 3rd use-case: any other node is removed
	    while (count < position) {
	        beforeNodeToDelete = currentNode;
	        nodeToDelete = currentNode.next;
	        count++;
	    }
	 
	    beforeNodeToDelete.next = nodeToDelete.next;
	    deletedNode = nodeToDelete;
	    nodeToDelete = null;
	    this._length--;
	 
	    return deletedNode;
	}
}


