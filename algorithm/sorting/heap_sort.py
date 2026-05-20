class HeapSort():
    def __init__(self, arr: list):
        self.raw = arr
        self.sorting = self.raw
        self.heapified = False
        self.len = len(arr)
        self.heap_end = self.len

    def sort(self):
        print(self.sorting)
        self.heapify()
        while self.heap_end > 1:
            self.sorting[0], self.sorting[self.heap_end-1] = self.sorting[self.heap_end-1], self.sorting[0]
            self.heap_end -= 1
            self.sift_down(1)
        
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
    
    def heapify(self):
        if self.heapified: return self.sorting
               
        # make sure the one deepest but have child
        cursor = self.parent(self.len)
        
        while cursor > 0:
            self.sift_down(cursor)
            cursor -= 1
        
        self.heapified = True

        return self.sorting
        
    def sift_down(self, cursor):
        print(self.sorting)
        if cursor > self.heap_end//2: return
        
        if cursor == self.heap_end/2:
            if self.sorting[self.child_left(cursor)-1] > self.sorting[cursor-1]:
                self.sorting[self.child_left(cursor)-1], self.sorting[cursor-1] = self.sorting[cursor-1], self.sorting[self.child_left(cursor)-1]
            return
        
        if self.sorting[self.child_left(cursor)-1] <= self.sorting[self.child_right(cursor)-1]:
            self.sorting[self.child_right(cursor)-1], self.sorting[cursor-1] = self.sorting[cursor-1], self.sorting[self.child_right(cursor)-1]
            self.sift_down(self.child_right(cursor))
        elif self.sorting[self.child_left(cursor)-1] > self.sorting[self.child_right(cursor)-1]:
            self.sorting[self.child_left(cursor)-1], self.sorting[cursor-1] = self.sorting[cursor-1], self.sorting[self.child_left(cursor)-1]
            self.sift_down(self.child_left(cursor))

        return
    
    # belows are all input position of heap instead of index of list.
    def child_left(self, a: int):
        return 2*a
    
    def child_right(self, a: int):
        return 2*a+1
    
    def parent(self, a: int):
        return a//2
    
    def left(self, a: int):
        return a-1
    
    def right(self, a: int):
        return a+1

if __name__ == "__main__":
    arr = [2,1,3,4,7,6,5,9,0]
    print(HeapSort(arr).sort())
    