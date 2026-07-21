class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r = len(image)
        c = len(image[0])
        original = image[sr][sc]
        
        if original == color:
            return image

        def dfs(i, j):
            if i < 0 or i >= r or j < 0 or j >= c:
                return 0

            if image[i][j] != original:
                return

            image[i][j] = color

            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)

        
        dfs(sr, sc)
    
        return image
        