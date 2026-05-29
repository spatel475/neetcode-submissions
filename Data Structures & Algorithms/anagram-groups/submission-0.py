class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}
        
        for item in strs:
            key = "".join(sorted(item))

            if key in result:
                result[key].append(item)
            else:
                result[key] = [item]

        return list(result.values())

        """
        create dict: key = sorted item, value = array of items from str 

        for each item in strs: 
            - sort item 
            - check if item in strs
            - if no, add to dict.
            - else, update dict value with new item
        
        return all values from dict as array

        """