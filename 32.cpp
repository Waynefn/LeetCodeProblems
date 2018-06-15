#include<stack>
using namespace std;
class Solution {
	
public:
	int longestValidParentheses(string s) {
		stack<int>stk;
		int lefts = 0;
		int sum,t,max=0;
		for (auto c : s) {
			if (c == '(') {
				lefts++;
				stk.push(0);
			}
			else {//c == ')'
				if (lefts <= 0) {
					lefts = 0;
					stk.push(-1);
				}
				else {
					t = stk.top();
					sum = 2;
					while(t>0) {
						stk.pop();
						sum += t;
						t = stk.top();
					}
					stk.pop();
					while (!stk.empty() && stk.top() > 0) {
						t = stk.top(); stk.pop();
						sum += t;
					}
					stk.push(sum);
					if (sum > max)
						max = sum;
					lefts--;
				}
				
			}
			
		}
		return max;
	}
};
