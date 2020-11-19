class Solution:
    def romanToInt(self,s:str)->int:
        result = 0
        prevS = ''
        romanNum = s.upper()
        #Error input
        if romanNum.find("IIII") != -1:
            return -1
        if romanNum.find("XXXX") != -1:
            return -1
        if romanNum.find("CCCC") != -1:
            return -1
        if romanNum.find("MMMM") != -1:
            return -1
        
        for x in romanNum:
            if x == 'M':
                if prevS == 'C':
                    result += 800
                    prevS = 'M'
                    continue
                prevS = 'M'
                result += 1000
                continue
            
            if x == 'D':
                #Error input
                if prevS == 'D':
                    return -1
                    
                if prevS == 'C':
                    result += 300
                    prevS = 'D'
                    continue
                prevS = 'D'
                result += 500
                continue
                
            if x == 'C':
                if prevS == 'X':
                    result += 80
                    prevS = 'C'
                    continue
                prevS = 'C'
                result += 100
                continue
                
            if x == 'L':
                #Error input
                if prevS == 'L':
                    return -1
                    
                if prevS == 'X':
                    result += 30
                    prevS = 'L'
                    continue
                prevS = 'L'
                result += 50
                continue
                
            if x == 'X':
                if prevS == 'I':
                    result += 8
                    prevS = 'X'
                    continue
                prevS = 'X'
                result += 10
                continue
                
            if x == 'V':
                #Error input
                if prevS == 'V':
                    return -1
                    
                if prevS == 'I':
                    result += 3
                    prevS = 'V'
                    continue
                prevS = 'V'
                result += 5
                continue
                
            if x == 'I':
                prevS = 'I'
                result += 1
                continue
        return result
