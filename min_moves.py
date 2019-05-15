class Sol:
    def min_moves(self,list):
        return sum(list)-min(list)*len(list)


if __name__ == '__main__':
    p1=Sol()
    print(p1.min_moves([1,2,3]))
