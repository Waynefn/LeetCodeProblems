ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    ListNode*ret=NULL;
    ListNode* p;
    while(l1!=NULL||l2!=NULL){
        if(ret==NULL){
            ret=new ListNode(0);
            p=ret;
        }
        else{
            p->next=new ListNode(0);
            p=p->next;
        }
        if(l2==NULL){
            p->val=l1->val; 
            l1=l1->next;
        }
        else if (l1==NULL){
            p->val=l2->val; 
            l2=l2->next;
        }
        else if(l1->val<l2->val){
            p->val=l1->val; 
            l1=l1->next;

        }
        else{
            p->val=l2->val; 
            l2=l2->next;
        }       
    }
    return ret;
}
