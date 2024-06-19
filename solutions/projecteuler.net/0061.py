def isPolygonal(num, p):
    a = [0.5,1,1.5,2,2.5,3]
    b = [0.5,0,-0.5,-1,-1.5,-2]
    c = -num
    D = [b[i]**2 - 4*a[i]*c for i in range(6)]
    if D[p-3] > 0:
        roots = [(-b[p-3] + D[p-3]**(1/2))/(2*a[p-3]), (-b[p-3] - D[p-3]**(1/2))/(2*a[p-3])]
        if (roots[0] >= 1 and roots[0] == int(roots[0]) or
            roots[1] >= 1 and roots[1] == int(roots[1])):
            return True
    return False

def cycleFinder(size, nums, unused):
    if not nums:
        for head in range(10, 99):
            for tail in range(10,99):
                num = int(str(head) + str(tail))
                for p in list(unused):
                    if isPolygonal(num, p):
                        unused.remove(p)
                        nums += [num]
                        cycleFinder(size, nums, unused)
                        unused.add(p)
                        nums[:] = nums[0:len(nums)-1]
    else:
        head = str(nums[-1])[2:]
        if len(nums) == size - 1:
            tail = str(nums[0])[0:2]
            num = int(head+tail)
            for p in unused:
                if isPolygonal(num, p):
                    nums += [num]
                    print(sum(nums))
                    nums[:] = nums[0:len(nums)-1]
            return
        else:
            for tail in range(10, 99):
                num = int(head + str(tail))
                for p in list(unused):
                    if isPolygonal(num, p):
                        unused.remove(p)
                        nums += [num]
                        cycleFinder(size, nums, unused)
                        unused.add(p)
                        nums[:] = nums[0:len(nums)-1]

nums = []
cycleFinder(6, nums, set([3,4,5,6,7,8]))

# 28684