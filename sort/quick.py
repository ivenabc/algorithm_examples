

class Quick: 
    @staticmethod
    def sort(a):
        length = len(a)
        Quick.sort_rec(a, 0, length-1)
    
    @staticmethod
    def sort_rec(a, lo, hi):
        if hi <= lo: return 
        j = Quick.partition(a, lo, hi)
        Quick.sort_rec(a, lo, j-1)
        Quick.sort_rec(a, j+1, hi)

    @staticmethod
    def partition(a, lo, hi):
        i = lo 
        j = hi + 1 
        v = a[lo]
        while True:
            i += 1 
            while Quick.less(a[i], v):
                if i == hi: break
                i +=1 
            j -= 1
            while Quick.less(v, a[j]):
                if j == lo: break
                j -= 1
            
            if i >= j: break
            Quick.exech(a, i, j)
        
        Quick.exech(a, lo, j)
        return j 
            

    @staticmethod
    def exech(a, i, j):
        a[i],a[j] = a[j], a[i]
    
    @staticmethod
    def less( data_i, data_j):
        return data_i < data_j



if __name__ == '__main__':
    a = [5,3,4,5,2,7,10,9,8]
    Quick.sort(a)
    print(a)