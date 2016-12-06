N = int(input())

array = list(map(int, input().split(' ')))

mean = sum(array)/N
print("{:.1f}".format(mean))

array.sort()
div = len(array)//2
median = sum(array[div-1:div+1])/2
print("{:.1f}".format(median))

cnt = [array.count(i) for i in array]
print("{}".format(array[cnt.index(max(cnt))]))
