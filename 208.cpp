class Trie {
	struct Node {
		Node*words[26];
		bool isEnd;
		Node() {
			isEnd = false;
			for (int i = 0;i<26;i++)
				words[i] = NULL;
		}
	};

public:
	/** Initialize your data structure here. */
	Node*Root;
	Trie() {
		Root = new Node;
	}

	/** Inserts a word into the trie. */
	void insert(string word) {
		Node*p = Root;
		for (char c : word) {
			if (p->words[c-'a'] == NULL) {
				p->words[c - 'a'] = new Node;
			}
			p = p->words[c - 'a'];
		}
		p->isEnd = true;
	}

	/** Returns if the word is in the trie. */
	bool search(string word) {
		Node*p = Root;
		for (char c : word) {
			if (p->words[c - 'a'] == NULL) {
				return false;
			}
			p = p->words[c - 'a'];
		}
		return p->isEnd;
	}

	/** Returns if there is any word in the trie that starts with the given prefix. */
	bool startsWith(string prefix) {
		Node*p = Root;
		for (char c : prefix) {
			if (p->words[c - 'a'] == NULL) {
				return false;
			}
			p = p->words[c - 'a'];
		}
		return true;
	}
};
