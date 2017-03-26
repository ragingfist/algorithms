
class Combination:

    def do(self, arr, start):
        for i in range(start, len(arr)):
            for j in range(start, i+1):
                print arr[j],
            print ' '

    def combo(self, arr):
        for k in range(len(arr)):
            self.do(arr, k)

    def choose(self, choose_num, arr, start, depth, output):
        if depth == choose_num:
            print output
            return
        for i in range(start, len(arr)):
            output.append(arr[i])
            self.choose(choose_num, arr, i+1, depth+1, output)
            output.pop()


array = ['a', 'b', 'c', 'd']

print "All combinations"
Combination().combo(array)
print
print "Choose X from a set of Y"
Combination().choose(2, array, 0, 0, [])

