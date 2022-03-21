from timeit import default_timer

nums1 = [2, 0]
m = 1
n = 1
nums2 = [1]

start = default_timer()
nums1_replica = nums1[:m]
runner1, runner2, writeRunner = 0, 0, 0

for writeRunner in range(m+n):
    if (runner2 >= n) or (runner1 < m and nums1_replica[runner1] <= nums2[runner2]):
        nums1[writeRunner] = nums1_replica[runner1]
        runner1 += 1
        writeRunner += 1
    else:
        nums1[writeRunner] = nums2[runner2]
        writeRunner += 1
        runner2 += 1

print(nums1)
end = default_timer()

print("Runtime - ", (end-start)*1000)