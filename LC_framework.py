'''
LeetCode刷题框架 :
这个模板，处理的是多组输入，或者多行输入；
如果是一组输入，仅仅几行的话， 就不用外层for循环的， 一行行的接收即可。

这个框架做到了主函数与处理问题的逻辑分离开。接收输入 -> 处理函数 -> 调整输出即可。 这么一来，我们在solve里就可以像在LeetCode上一样，直接写解决问题的函数。这样的代码看起来清晰，找bug时也好找。
另外，就是一定要重视低耦合高内聚的编程技巧。如果遇到处理不同的事情，尽量的写成函数的方式，这样调试起来会更加简洁。
'''
import sys


# 这里写解决问题的代码，和LeetCode就完全一样了
def solve(arr):
    pass


if __name__ == '__main__':
    # 接收输入时都是一行一行地接收
    # 接收输入的逻辑，这里先把输入接收过来， 两种选择input()和sys.stdin.readline()
    group_nums = input()  # 字符串形式，得转成int
    # group_nums就是接收多少组数据
    group_nums = int(group_nums)

    # 对于每一组数据
    for i in range(group_nums):
        # 接收每一组的输入, 这里不同的题目就不一样了，但一定记住我们接收的还是一行，这是一个字符串
        arr = sys.stdin.readline().strip().split(' ')
        # 元素转成int
        arr = list(map(int, arr))

        # 输入接收过来之后，这里最好打印下看看接收的是不是正确，这个很重要
        # print(arr)

        # 处理具体的问题了
        res = solve(arr)

        # 输出结果
        print(res)
