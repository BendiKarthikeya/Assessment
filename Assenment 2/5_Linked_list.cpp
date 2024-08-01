class node{
    public:
    int val;
    node* next;
    node(int data){
        val=data;
        next=NULL;
    }
};

class MyLinkedList {
public:
    node* head;
    MyLinkedList() {
        head=NULL;
    }
    int length(){
        int count=0;
        node* temp=head;
        while(temp!=NULL){
            count++;
            temp=temp->next;
        }
        return count;
    }
    
    int get(int i) {
        int len= length();
        if(head==NULL) return -1;
        else if(len<i) return -1;
        else{
            int count=0;
            node* temp=head;
            while(count<i){
                temp=temp->next;
                count++;
            }
            if(temp==NULL) return -1;
            return temp->val;
        }
    }
    
    void addAtHead(int val) {
        node* newNode=new node(val);
        newNode->next=head;
        head=newNode;
    }
    
    void addAtTail(int val) {
        node* newNode=new node(val);
        if(head==NULL){
            head=newNode;
        }
        else{
            node* temp=head;
            while(temp->next!=NULL){
                temp=temp->next;
            }
            temp->next=newNode;
        }
    }
    
    void addAtIndex(int i, int val) {
        node* newNode=new node(val);
        if(i==0){
            addAtHead(val);
        }
        else{
            int count=0;
            node* temp=head;
            while(temp!=NULL && count<i-1){
                temp=temp->next;
                count++;
            }
            if(temp==NULL) return;
            node* temp1=temp->next;
            temp->next=newNode;
            newNode->next=temp1;
        }
    }
    
    void deleteAtIndex(int i) {
        if(head==NULL) return;
        else if(i==0){
            node* temp=head;
            head=head->next;
            delete temp;
        }
        else{
            int count=0;
            node* temp=head;
            while(count<i-1){
                temp=temp->next;
                count++;
            }
            if(temp==NULL || temp->next==NULL) return;
            node* temp1=temp->next;
            temp->next=temp->next->next;
            delete temp1;
        }
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */