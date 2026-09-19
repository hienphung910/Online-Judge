# In tan 9 chu so thap phan - vi du 2.333333333 so voi dap an 2.333333.
# Sai so 3.3e-10 < 1e-6 nen van AC: minh hoa FloatComparator.
import sys

data = sys.stdin.read().split()
n = int(data[0])
nums = [int(x) for x in data[1:1 + n]]
print("%.9f" % (sum(nums) / n))
