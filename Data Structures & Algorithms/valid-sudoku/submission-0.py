class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,len(board)):
            seen = set()
            for j in range(0,len(board)):
                if board[i][j] in seen:
                    return False
                elif board[i][j] != ".":
                    seen.add(board[i][j])
        for i in range(0,len(board)):
            seen = set()
            for j in range(0,len(board)):
                if board[j][i] in seen:
                    return False
                elif board[j][i] != ".":
                    seen.add(board[j][i])
        box = {}
        for i in range(0,len(board)):
            box[i] = []
        for i in range(0,len(board)):
            for j in range(0,len(board)):
                if board[i][j] != ".":
                    index = (i // 3) * 3 + (j // 3)
                    if board[i][j] in seen:
                        return False
                    else :
                        box[index].append(board[i][j])
                
        return True

        
            
            
        

            
            


        