import random

class QuickSort():
    def __init__(self, arr: list):
        self.raw = arr
        self.sorting = self.raw

    def sort(self):
        print(self.sorting)
        need_sort_len = len(self.sorting)
        
        if need_sort_len <= 1:
            return self.sorting
        
        pivot_pos = random.randint(0, need_sort_len-1)
        pivot = self.sorting[pivot_pos]
        
        left, right = [], []
        
        remain = self.sorting.copy()
        remain.remove(pivot)
        
        for i in remain:
            if i > pivot:
                right.append(i)
                continue
            left.append(i)
                
        
        left = QuickSort(left).sort()
        right = QuickSort(right).sort()
        
        self.sorting = left + [pivot] + right

        return self.sorting

    def check(self):
        prev = None
        for i in self.sorting:
            if prev is None: 
                prev = i
                continue
            if i < prev:
                return False
            prev = i

        return True

if __name__ == "__main__":
    arr = [2,1,3,4,7,6,5,9,8,0]
    print(QuickSort(arr).sort())
    