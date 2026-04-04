class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        digits = set("123456789")

        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item not in digits:
                    continue

                item =  int(item)
                if item in rows[i]:
                    return False
                else:
                    rows[i].add(item)
                if item in cols[j]:
                    return False
                else:
                    cols[j].add(item)
                if item in boxes[i//3][j//3]:
                    return False
                else:
                    boxes[i//3][j//3].add(item)
        return True
                