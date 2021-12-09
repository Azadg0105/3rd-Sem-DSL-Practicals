#include <iostream>
using namespace std;

class Node
{
   public:
   int data;
   Node *next;
};

Node* head = NULL;
void insert(int new_data)
{
   Node* new_node = (Node*) malloc(sizeof(Node));
   //Node* new_node= new Node(new_data);
   new_node->data = new_data; 
   new_node->next = head;
   head = new_node;
}
void display()
{
   Node* ptr;
   ptr = head;
   while (ptr != NULL)
   {
      cout<< ptr->data <<" ";
      ptr = ptr->next;
   }
}

int main() 
{
   int n,num,i;
   cout<<"How many numbers do u want to insert: ";
   cin>>n;
   for(i=0;i<n;i++)
   {
       cout<<"Enter the number: ";
       cin>>num;
       insert(num);
   }
   //insert(9);
   cout<<"The linked list is: ";
   display();
   return 0;
}




