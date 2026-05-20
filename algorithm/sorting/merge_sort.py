class MergeSort():
    def __init__(self, arr: list):
        self.raw = arr
        self.sorting = self.raw

    def sort(self):
        print(self.sorting)
        need_sort_len = len(self.sorting)
        
        if need_sort_len == 1:
            return self.sorting
        
        left = list(self.sorting[:need_sort_len//2])
        right = list(self.sorting[need_sort_len//2:])
        
        left = MergeSort(left).sort()
        right = MergeSort(right).sort()
        
        self.sorting = []
        left_pos, right_pos = 0, 0
        while left_pos + right_pos != need_sort_len:
            if left_pos == len(left):
                self.sorting.append(right[right_pos])
                right_pos+=1
                continue
            
            if right_pos == len(right):
                self.sorting.append(left[left_pos])
                left_pos+=1
                continue
            
            if left[left_pos] < right[right_pos]:
                self.sorting.append(left[left_pos])
                left_pos+=1
                continue
            
            self.sorting.append(right[right_pos])
            right_pos+=1

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
    print(MergeSort(arr).sort())
    