'''
在一个小镇里，按从 1 到 N 标记了N个人。传言称，这些人中有一个是小镇上的秘密法官。

如果小镇的法官真的存在，那么：
    小镇的法官不相信任何人。
    每个人（除了小镇法官外）都信任小镇的法官。
    只有一个人同时满足属性 1 和属性 2 。
给定数组trust，该数组由信任对 trust[i] = [a, b]组成，表示标记为 a 的人信任标记为 b 的人。

如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1。
输入：N = 2, trust = [[1,2]]
输出：2
输入：N = 3, trust = [[1,3],[2,3]]
输出：3
输入：N = 3, trust = [[1,3],[2,3],[3,1]]
输出：-1
输入：N = 3, trust = [[1,2],[2,3]]
输出：-1
输入：N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
输出：3
1 <= N <= 1000
trust.length <= 10000
trust[i]是完全不同的
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N、
'''

N = 4   # pos样例
trust = [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
    [4, 3]
]
# N = 3   # neg样例
# trust = [
#     [1, 3],
#     [2, 3],
#     [3, 1]
# ]

'''自己写的答案：暴力遍历'''
# dict_trust_who = {k:[] for k in range(1,N+1)}
# # print(dict_trust_who)
# for i in trust:
#     which_guy, trust_who = i
#     dict_trust_who[which_guy].append(trust_who)
# who_maybe_judge = 0
# for key,list in dict_trust_who.items():
#     if list == []:
#         who_maybe_judge = key
# tag = 0
# for key,list in dict_trust_who.items():
#     if who_maybe_judge in list:
#         tag += 1
# if tag == N-1:
#     print(who_maybe_judge)
# else:
#     print(-1)


'''答案1 ：和我想法差不多但是写的 very pythonic'''

j = list(set(n+1 for n in range(N)) - set(t[0] for t in trust)) # 找到疑似法官
print(j)
# 第一层 if 如果j不是一个 return -1
# 第二层 if (第一层if条件已满足)如果信任j的所有人加起来不是N-1 return -1
print(-1 if len(j)!=1 else j[0] if len(set(t[0] for t in trust if t[1]==j[0]))+1 == N else -1)


'''答案2 ： 本质是有向图的入度（被别人信任）和出度（我信任谁）的问题，总结一下性质：

法官： 出度为0，入度为n-1 ， 对应差值就是 n-1
其他人： 出度不为0. 入度最大只能是n-2,对应差值就是 n-2-i 必然小于 n-1
那么我们就维护一个数组记录这个差值就可以，然后差值为n-1的就是法官
'''

# # 记录入度-出度的差值,故意多留一个无需减1
# if N == 1: print(1)
# cnt = [0 for i in range(N+1)]
# for i in trust:
#     cnt[i[0]] -= 1 # 出度是减（信任别人）
#     cnt[i[1]] += 1 # 入度是加 （不信任）
# print(cnt)
# for index,degree in enumerate(cnt):
#     if degree == N-1:
#         print(index) # 应该是return
# print(-1) # 应该是return