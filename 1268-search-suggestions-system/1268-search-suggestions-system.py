class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        
        print(products)
        # 1. Sorting the products lexicographically
        products = sorted(products)
        print(products)
        
        # 2. Run a for loop for each character from the searchWord
        masterMatch = []
        for charIndex in range(1, len(searchWord)+1):
            matches = []
            for product in products:
                if len(matches) == 3:
                    break
                if charIndex > len(product):
                    continue
                if searchWord[:charIndex] == product[:charIndex]:
                    matches.append(product)
            masterMatch.append(matches)
        
        return masterMatch