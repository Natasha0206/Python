hashmap = set()
class Node:
	
	def __init(self):
		self.data = 0
		self.next = None

def push(head_ref, new_data):

	new_node = Node()

	new_node.data = new_data;
	new_node.next = (head_ref);

	(head_ref) = new_node;
	
	return head_ref

def deleteNode(head_ref, delt):

	temp = head_ref;

	if (head_ref == None or delt == None):
		return;

	if (head_ref == delt):
		head_ref = delt.next;

	while (temp.next != delt):
		temp = temp.next;

	temp.next = delt.next;

	del(delt);

	return;

def largestElement(head_ref):


	max = -10000000

	head = head_ref;


	while (head != None):

		if (max < head.data):
			max = head.data;

		head = head.next;
	
	return max;


def createHash(maxElement):


	prev = 0
	curr = 1;
	hashmap.add(prev);
	hashmap.add(curr);

	while (curr <= maxElement):
		temp = curr + prev;
		hashmap.add(temp);
		prev = curr;
		curr = temp;

def printFibonacci(head_ref):

	count = 0;
	ptr = head_ref
	
	print("Fibonacci nodes = ",end='')

	while (ptr != None):

		if (ptr.data in hashmap):
			print(ptr.data, end=' ')

		ptr = ptr.next;
		
	print()

	return 0;

def countFibonacci(head_ref):

	count = 0;
	ptr = head_ref;

	while (ptr != None):

		if (ptr.data in hashmap):

			count += 1

		ptr = ptr.next;

	return count;

def minmaxFibonacciNodes(head_ref):
	maxEle = largestElement(head_ref);
	minimum = 100000000
	maximum = -100000000
	ptr = head_ref;

	while (ptr != None):

		if (ptr.data in hashmap):
			minimum = min(minimum, ptr.data);
			maximum = max(maximum, ptr.data);
		
		ptr = ptr.next;
	
	print("Minimum Fibonacci node: "+str(minimum))
	print("Maximum Fibonacci node: "+str(maximum))
def deleteFibonacciNodes(head_ref):

	ptr = head_ref;
	next = None

	while (ptr != None):
		next = ptr.next;

		if (ptr.data in hashmap):
			
			deleteNode(head_ref, ptr);

		ptr = next;

def printList(head):

	while (head != None):
		print(head.data, end = ' ')
		head = head.next;
	
def operations(head):

	maxEle = largestElement(head);
	createHash(maxEle);

	printFibonacci(head);

	print("Count of Fibonacci nodes = " + str(countFibonacci(head)))

	minmaxFibonacciNodes(head);

	deleteFibonacciNodes(head);
	print("List after deletion: ", end='')

	printList(head);


if __name__=='__main__':
	

	head = None;

	head = push(head, 13);
	head = push(head, 6);
	head = push(head, 8);
	head = push(head, 16);
	head = push(head, 15);

	operations(head);