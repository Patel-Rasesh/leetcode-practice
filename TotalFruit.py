class Solution(object):
    def totalFruit(self, fruits):
        basket = set()
        output = []
        if len(set(fruits)) == 1:
            return len(fruits)
        for parent in range(len(fruits)):
            basket.add(fruits[parent])
            for child in range(parent+1, len(fruits)):
                basket.add(fruits[child])
                if len(basket) > 2:
                    basket = set()
                    output.append(child-parent)
                    break
                if child == len(fruits) -1:
                    basket = set()
                    output.append(child-parent+1)
                    break
        if output:
            return max(output)
        else:
            return 0
    
obj = Solution()
fruits = [0]
print(obj.totalFruit(fruits))