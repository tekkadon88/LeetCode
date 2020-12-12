"""
733. Flood Fill

URL: https://leetcode.com/problems/flood-fill/
Level: Easy
"""
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # ターゲットのピクセルがすでに目的の色だったら何もせずにリストを返す
        if image[sr][sc] == newColor:
            return image
        
        def dfs(row, col):
            if image[row][col] == color:
                image[row][col] = newColor
                if row >= 1: # 1つ上
                    dfs(row-1, col)
                if row +1 < len(image): # 1つ右
                    dfs(row+1, col)
                if col >=1: # 1つ左
                    dfs(row, col-1)
                if col+1 < len(image[0]): # 1つ下
                    dfs(row, col+1)

        # 元々の色
        color = image[sr][sc]
        # スタート (sr, sc) から順番にピクセルをみていき、同じ色の場合は目的の色に塗り替える
        dfs(sr, sc)
        return image

if __name__ == '__main__':
    solution = Solution()
    pixels = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    print(solution.floodFill(pixels, sr, sc, newColor))