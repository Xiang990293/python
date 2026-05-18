import random

class BogoSort():
    def __init__(self, arr: list):
        self.raw = arr
        self.sorting = self.raw

    def sort(self):
        print(self.sorting)
        while not self.check():
            random.shuffle(self.sorting)
            print(self.sorting)
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
    arr = [1,2,4,3]
    print(BogoSort(arr).sort())