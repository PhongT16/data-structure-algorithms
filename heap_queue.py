class myHeapQueue:

    @staticmethod
    def heapify(arr: list[int]):
        print(f"Starting heapify")
        print(f"Length of arr: {len(arr)}")
        for index in range(len(arr) - 1, -1, -1):
            if (2 * index) + 1 >= len(arr) and (2 * index) + 2 >= len(arr):
                # leaf node
                continue
        
            left_child = (2 * index) + 1
            right_child = (2 * index) + 2

            cur_index = index

            # if left child is out of bounds, then right child is also out of bounds
            while left_child < len(arr):
                if right_child < len(arr):
                    if arr[left_child] <= arr[right_child] and arr[left_child] < arr[cur_index]:
                        tmp = arr[cur_index]
                        arr[cur_index] = arr[left_child]
                        arr[left_child] = tmp
                        cur_index = left_child
                        left_child = (2 * cur_index) + 1
                        right_child = (2 * cur_index) + 2
                    elif arr[right_child] <= arr[left_child] and arr[right_child] < arr[cur_index]:
                        tmp = arr[cur_index]
                        arr[cur_index] = arr[right_child]
                        arr[right_child] = tmp
                        cur_index = right_child
                        left_child = (2 * cur_index) + 1
                        right_child = (2 * cur_index) + 2
                    else:
                        break
                elif arr[left_child] < arr[cur_index]:
                    tmp = arr[cur_index]
                    arr[cur_index] = arr[left_child]
                    arr[left_child] = tmp
                    cur_index = left_child
                    left_child = (2 * cur_index) + 1
                    right_child = (2 * cur_index) + 2
                else:
                    break
    @staticmethod
    def heapppush(arr: list[int], value: int) -> None:
        # Assumes arr has been heapified
        if arr is None:
            raise ValueError("arr cannot be None")

        arr.append(value)
        index = len(arr) - 1
        parent_index = (index - 1) // 2
        
        while parent_index >= 0 and arr[index] < arr[parent_index]:
            # switch new node with parent node
            tmp = arr[index]
            arr[index] = arr[parent_index]
            arr[parent_index] = tmp

            index = parent_index
            parent_index = (index - 1) // 2

    @staticmethod
    def heappop(arr: list[int]):
        # Assumes arr has been heapified

        if not arr:
            raise ValueError("arr is empty. Nothing to pop.")
        
        min_number = arr[0]
        arr[0] = arr[-1]
        index = 0
        arr.pop()
        left_child = (2 * index) + 1
        right_child = (2 * index) + 2

        cur_index = index

        while left_child < len(arr):
            if right_child < len(arr):
                if arr[left_child] <= arr[right_child] and arr[left_child] < arr[cur_index]:
                    tmp = arr[cur_index]
                    arr[cur_index] = arr[left_child]
                    arr[left_child] = tmp
                    cur_index = left_child
                    left_child = (2 * cur_index) + 1
                    right_child = (2 * cur_index) + 2
                elif arr[right_child] <= arr[left_child] and arr[right_child] < arr[cur_index]:
                    tmp = arr[cur_index]
                    arr[cur_index] = arr[right_child]
                    arr[right_child] = tmp
                    cur_index = right_child
                    left_child = (2 * cur_index) + 1
                    right_child = (2 * cur_index) + 2
                else:
                    break
            elif arr[left_child] < arr[cur_index]:
                tmp = arr[cur_index]
                arr[cur_index] = arr[left_child]
                arr[left_child] = tmp
                cur_index = left_child
                left_child = (2 * cur_index) + 1
                right_child = (2 * cur_index) + 2
            else:
                break
        return min_number

    @staticmethod
    def heappeek(arr: list[int]) -> int:
        return arr[0]


'''
Implementing a min-heap.

Attributes:
- Complete Tree
- Parent node is smaller than its children

Assumptions
1. The input is an array representation of a binary tree.
2. The array is an in-order traversal of the binary tree.

# Math
Given a node a the i-th index, the left child is at 2i + 1 and the right
child is at 2i + 2.
Given a node at the i-th index, it's parent is located at floor((i - 1) / 2)

'''
