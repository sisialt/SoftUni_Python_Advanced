from collections import deque


def list_manipulator(nums, add_or_remove, end_or_beg, *args):
    result = deque(nums)
    args = deque(args)

    if add_or_remove == "add":

        if end_or_beg == "beginning":
            while args:
                result.appendleft(args.pop())

        elif end_or_beg == "end":
            result.extend(list(args))

    elif add_or_remove == "remove":

        if end_or_beg == "beginning":
            if args:
                for i in range(args[0]):
                    result.popleft()
            else:
                result.popleft()

        elif end_or_beg == "end":
            if args:
                for i in range(args[0]):
                    result.pop()
            else:
                result.pop()

    return list(result)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
