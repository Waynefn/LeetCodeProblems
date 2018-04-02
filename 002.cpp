ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    int val=l1->val+l2->val;
    int carry=val>=10;
    val%=10;
    ListNode*ret=new ListNode(val);
    ListNode*p=ret;
    while(l1->next!=NULL || l2->next!=NULL){
        if(l1->next!=NULL)l1=l1->next;else l1->val=0;
        if(l2->next!=NULL)l2=l2->next;else l2->val=0;
        val=l1->val+l2->val+carry;
        carry=val>=10;
        val%=10;
        p->next=new ListNode(val);
        p=p->next;
    };
    if(carry>0)
        p->next=new ListNode(carry);
    return ret;
}
