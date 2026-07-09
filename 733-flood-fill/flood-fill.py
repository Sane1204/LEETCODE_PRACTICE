class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows=len(image)
        cols= len(image[0])
        original = image[sr][sc]
        if original==color:
            return image
        def explore(sr,sc):
            if sr<0 or sr>=rows:
                return
            if sc<0 or sc>=cols:
                return
            if image[sr][sc]!= original:
                return 
                

            image[sr][sc]= color

            explore(sr+1,sc)
            explore(sr-1,sc)
            explore(sr,sc+1)
            explore(sr,sc-1)
        
        explore(sr,sc)
        return image   
        