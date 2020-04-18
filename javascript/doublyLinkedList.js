function Node(value) {
    this.data = value;
    this.previous = null;
    this.next = null;
}
 
function DoublyList() {
    this._length = 0;
    this.head = null;
    this.tail = null;
}
 
DoublyList.prototype = {
    constructor : DoublyList,
    add : function(value) {
        process.stdout.write('adding node with data :'+value+'\n');
        var node = new Node(value);
     
        if (this._length) {
            this.tail.next = node;
            node.previous = this.tail;
            this.tail = node;
        } else {
            this.head = node;
            this.tail = node;
        }
     
        this._length++;
     
        return node;
    },
     
    searchNodeAt : function(position) {
        var currentNode = this.head,
            length = this._length,
            count = 1,
            message = {failure: 'Failure: non-existent node in this list.'};
     
        // 1st use-case: an invalid position
        if (length === 0 || position < 1 || position > length) {
            throw new Error(message.failure);
        }
     
        // 2nd use-case: a valid position
        while (count < position) {
            currentNode = currentNode.next;
            count++;
        }
     
        return currentNode;
    },
     
    remove : function(position) {
        process.stdout.write('removing node at position :'+position+'\n');
        var currentNode = this.head,
            length = this._length,
            count = 1,
            message = {failure: 'Failure: non-existent node in this list.'},
            beforeNodeToDelete = null,
            nodeToDelete = null,
            deletedNode = null;
     
        // 1st use-case: an invalid position
        if (length === 0 || position < 1 || position > length) {
            throw new Error(message.failure);
        }
     
        // 2nd use-case: the first node is removed
        if (position === 1) {
            this.head = currentNode.next;
     
            // 2nd use-case: there is a second node
            if (!this.head) {
                this.head.previous = null;
            // 2nd use-case: there is no second node
            } else {
                this.tail = null;
            }
     
        // 3rd use-case: the last node is removed
        } else if (position === this._length) {
            this.tail = this.tail.previous;
            this.tail.next = null;
        // 4th use-case: a middle node is removed
        } else {
            while (count < position) {
                currentNode = currentNode.next;
                count++;
            }
     
            beforeNodeToDelete = currentNode.previous;
            nodeToDelete = currentNode;
            afterNodeToDelete = currentNode.next;
     
            beforeNodeToDelete.next = afterNodeToDelete;
            afterNodeToDelete.previous = beforeNodeToDelete;
            deletedNode = nodeToDelete;
            nodeToDelete = null;
        }
     
        this._length--;
     
        return message.success;
    },
    display : function () {
        console.log('displaying list');

        if(this._length === 0 ) 
        {   
            process.stdout.write('Empty List');
            return;
        }
        
        if(this._length === 1) {
            process.stdout.write(this.head.data);
            return;
        }
        var currentNode = this.head;

        while(currentNode.next) {
            process.stdout.write("<-"+currentNode.data+"->");
            currentNode = currentNode.next;
        }
        process.stdout.write("<-"+currentNode.data+"->");
    }
};

var dlist1 = new DoublyList();

dlist1.add(1);
dlist1.add(2);
dlist1.add(3);
dlist1.add(4);
dlist1.add(5);
dlist1.add(6);

process.stdout.write('Node at position 3 has data '+dlist1.searchNodeAt(3).data+'\n');

dlist1.remove(4);
dlist1.display();