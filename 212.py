class Solution:
    def dfs(self, word, wid, x, y, VISIT):
        if wid == len(word):
            if self.reverse:
                self.RESULT.append(word[::-1])
            else:
                self.RESULT.append(word)
            raise TimeoutError
        for movx,movy in ((-1,0),(0,-1),(1,0),(0,1)):
            nx, ny = x + movx, y + movy
            if (nx, ny) not in VISIT and self.board[nx][ny] == word[wid]:
                VISIT.add((nx, ny))
                self.dfs(word, wid + 1, nx, ny, VISIT)
                VISIT.remove((nx, ny))

    def check(self, word):
        for i in range(1,self.SIZE[0]+1):
            for j in range(1,self.SIZE[1]+1):
                if self.board[i][j] == word[0]:
                    VISIT = set()
                    VISIT.add((i,j))
                    self.dfs(word, 1, i, j, VISIT)
                    
    def __init__(self):
        self.RESULT=[]
        self.board=[]
        
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.SIZE = (len(board), len(board[0]))
        self.board.append([';'] * (self.SIZE[1]+2)) # Here I use a padding board to save some time on boarder check. 
                                                    #It seems that this method is not marked to decrease time.
        for lines in board:
            self.board.append([';']+lines+[';'])
        self.board.append([';'] * (self.SIZE[1]+2))
        for word in sorted(words,key=lambda x:len(x),reverse=True):
            try:
                for w in self.RESULT:
                    if word in w or word[::-1] in w:
                        if word !=w:
                            self.RESULT.append(word)
                        raise ValueError
                if re.match(r"^(.)\1{4}",word):  # words like aaaaaaaaab costs much time. I just reverse them.
                    self.reverse = True
                    self.check(word[::-1])
                else:
                    self.reverse = False
                    self.check(word)
            except: continue
        return self.RESULT
