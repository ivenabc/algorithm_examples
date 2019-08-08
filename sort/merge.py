
class Merge:
    @staticmethod
    def less( data_i, data_j):
        return data_i < data_j

    def show(self):
        print(self.__list)
    
    def is_sorted(self):
        for i in range(1, len(self.__list)):
            if(self.less(i, i-1)):
                return False
    
    def get_list(self):
        return self.__list

    @staticmethod
    def merge(a, aux, lo, mid, hi):
        for k in range(lo, hi+1, 1):
            print(lo, hi)
            aux[k] = a[k]
        
        i = lo
        j = mid+1
        for k in range(lo, hi+1, 1):
            if i > mid: 
                a[k] = aux[j]
                j += 1
            elif j > hi: 
                a[k] = aux[i]
                i += 1
            elif Merge.less(aux[j], aux[i]): 
                a[k] = aux[j]
                j += 1
            else: 
                a[k] = aux[i] 
                i += 1
    
    @staticmethod
    def sort_rec(a, aux, lo, hi):
        if hi <= lo: return 
        mid = lo + (hi-lo) // 2 
        Merge.sort_rec(a, aux, lo, mid)
        Merge.sort_rec(a, aux, mid+1, hi)
        Merge.merge(a, aux, lo, mid, hi)
    
    @staticmethod
    def sort(a):
        length = len(a)
        aux = [0]*length
        Merge.sort_rec(a, aux, 0, length-1)

        
if __name__ == '__main__':
    a = [1,3,4,5,2,7,10,9,8]
    Merge.sort(a)
    print(a)