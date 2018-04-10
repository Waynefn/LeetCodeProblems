/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
	struct ListNode* front=head,*back=head;
	while (n-- > 0)
		front = front->next;
	if (front == NULL)return head->next;
	while (front->next != NULL) {
		front = front->next;
		back = back->next;
	}
	back->next = back->next->next;
	return head;
}
