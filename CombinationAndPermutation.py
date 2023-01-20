def C(nums):
	ans = []

	def dfs(n, s, cur):
		if len(cur) == n:
			ans.append(cur.copy())
			return

		for i in range(s, len(nums)):
			cur.append(nums[i])
			dfs(n, i + 1, cur)
			cur.pop()

	for i in range(0, len(nums)):
		dfs(i, 0, [])


	print(ans, end="\n")


def P(nums):
	res = []
	cur = []
	used = [False] * len(nums)

	def dfs(i):
		if i == len(nums):
			res.append(cur.copy())
			return

		if used[i]:
			return

		used[i] = True
		cur.append(nums[i])
		dfs(i+1)
		cur.pop()
		used[i] = False
		dfs(i+1)

	dfs(0)
	print(res)

if __name__ == '__main__':
	nums = [1, 2, 3]
	C(nums)
	P(nums)