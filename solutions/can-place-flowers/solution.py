class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        j=0
        if sum(flowerbed)==0:
            return (len(flowerbed)+1)//2>=n if len(flowerbed)%2==1 else (len(flowerbed))//2>=n


        for i in range(len(flowerbed)-2):
            
            
            if i==0 and flowerbed[0]+flowerbed[1]==0:
                j+=1
                flowerbed[0]=1
            elif i==len(flowerbed)-3 and flowerbed[i+1]+flowerbed[i+2]==0:
                j+=1
                flowerbed[-1]=1
            elif flowerbed[i]+flowerbed[i+1]+flowerbed[i+2]==0:
                j+=1
                flowerbed[i+1]=1
        return j>=n
        