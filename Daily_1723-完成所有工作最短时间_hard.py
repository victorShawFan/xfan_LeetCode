'''
【方法：二分+递归回溯+剪枝】
给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。
请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。
返回分配方案中尽可能 最小 的 最大工作时间 。
1 <= k <= jobs.length <= 12
1 <= jobs[i] <= 107

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

jobs = [1,2,4,7,8] # jobs[i] 是完成第 i 项工作要花费的时间
k = 2 # 将这些工作分配给 k 位工人
A: 11 # 解释：按下述方式分配工作：
1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
2 号工人：4、7（工作时间 = 4 + 7 = 11）
最大工作时间是 11 。

jobs = [3,2,3]
k = 3
A: 3 # 解释：给每位工人分配一项工作，最大工作时间是 3 。

# 使工人的 最大工作时间 得以 最小化，返回分配方案中尽可能 最小 的 最大工作时间
# 甘特图？
'''
# 回溯就是让计算机自动的去搜索，碰到符合的情况就结束或者保存起来，
# 在一条路径上走到尽头也不能找出解，就回到原来的岔路口，选择一条以前没有走过的路继续探测，直到找到解或者走完所有路径为止。
# 回溯要尽量剪枝，不然这个阶乘复杂度肯定爆

# DFS（TLE）
# 一看数据范围只有 1212，我猜不少同学上来就想 DFS，但是注意 n 和 k 同等规模的，爆搜（DFS）的复杂度是 O(k^n)的。会卡死效率

def backtrace(arr, groups, limit): # 尝试每种可能性
    print('arr :',arr,'groups :',groups,'limit :',limit)
    if not arr:return True # 分完则方案可行
    v= arr.pop()  # 从sorted_jobs的末尾拿出当前最大的
    for i in range(len(groups)):  # 遍历当前工人
        if groups[i] + v <= limit : #如果当前工人的workload+最大的 小于 limit
            groups[i] += v # 就加上
            if backtrace(arr,groups,limit): # 递归进入
                return True
            groups[i] -= v
            if groups[i] == 0: # ！剪枝，如果这个工人没分到活，那别人肯定得多干活了，那最后的结果必然不是最小的最大值，就不用继续试了。
                break
    arr.append(v)
    return False



def check(limit,jobs,k): # 定义一个K大小的数组，然后做回溯，每个元素的值不超过limit，我们就往下试
    arr = sorted(jobs)       # ！剪枝：排序后，大的先拿出来试，如果方案不行，失败得更快，fail fast，实测加上这个剪枝会快3倍
    print('init_arr : ',arr)
    groups = [0] * k      # 有K个人干活，分成K组，看看在这个limit 下 能不能安排完工作
    print('init_groups : ', groups)
    if backtrace(arr,groups,limit): # 进入回溯
        return True
    else:
        return False


def main():
    '''这个解法的本质也是暴搜，只不过优化了效率，就是先猜答案 最小时间(limit)，然后看在这个答案情况下能不能把工作分完'''
    jobs = [1, 2, 4, 7, 8]
    k = 2  # 结果应当是 p1 = 1+2+8 =11 ,p2 = 4+7 =11
    # begin 想象一下 K 个人，可以设置一个每个人最大运输量大小为limit，如果在这个limit下，工作能分完，这个方案是可行的，如果在这个limit 下分不完，那这个方案不可行
    l,r = max(jobs),sum(jobs)   # 人均工作量的上限的范围，最小为job的最大值(少于则分不完)，最大为jobs之和(全部分给一个人其他不干)
    # 可以在区间[min_limit,max_limit]里面一个个试来找到第一个满足要求的limit，但是会超时，所以用二分搜索加速
    check_time = 0
    while l< r:  # 二分法 ： 加速找到limit
        print('区间 : ',l,r)
        mid = (l+r) // 2  # 此时 mid  = limit
        print('current limit :',mid)
        if check(mid,jobs,k): # 判断在这个limit下工作能不能分完
            r = mid # 分的完就继续寻找下一个更小的最优Limit
        else:
            l= mid + 1 # 分不完就继续寻找下一个更大的最优Limit
        check_time += 1
    print(check_time)
    print(l) # 最后会有一个l=r=limit



if __name__ == '__main__':
    main()


'''
还有的比较有意思的解法为 状态压缩dp和模拟退火和剪枝DFS
'''