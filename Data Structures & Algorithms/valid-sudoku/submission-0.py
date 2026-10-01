class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = []
        i=0
        while i < 9:
            for num in board[i]:
                if num == '.':
                    continue
                elif num in check:
                    return False
                else:
                    check.append(num)
            check.clear()
            i+=1

        i=0  
        while i < 9:
            j=0
            check.clear()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                elif board[j][i] in check:
                    return False
                else:
                    check.append(board[j][i])
            check.clear()
            i+=1
       
        group = [
            [0,0],[0,1],[0,2],
            [1,0],[1,1],[1,2],
            [2,0],[2,1],[2,2]
        ]

        for x in range(0,7,3):
            for j in range(0,7,3):
                for i in range(9):
                    if board[(group[i][0])+x][(group[i][1])+j] == '.':
                            continue
                    elif board[(group[i][0])+x][(group[i][1])+j] in check:
                        return False
                    else:
                        check.append(board[(group[i][0])+x][(group[i][1])+j])
                check.clear()
        return True
        
        
        