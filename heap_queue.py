def heapify(arr: list[int]):
    pass
    

def heap_push(arr: list[int], value: int) -> None:
    # Assumes arr has been heapified
    arr.append(value)
    index = len(arr) - 1
    parent_index = (index - 1) // 2
    
    while parent_index >= 0 and (arr[parent_index] is None or arr[index] < arr[parent_index]):
        # switch new node with parent node
        tmp = arr[index]
        arr[index] = arr[parent_index]
        arr[parent_index] = tmp

        index = parent_index
        parent_index = (index - 1) // 2

def heap_pop(arr: list[int]):
    # Assumes arr has been heapified

    if not arr:
        raise ValueError("arr is empty. Nothing to pop.")
    
    min_number = arr[0]
    index = 0
    left_child = (2 * index) + 1
    right_child = (2 * index) + 2

    while left_child < len(arr) or right_child < len(arr):
        if left_child >= len(arr):
            min_child = right_child
        elif right_child >= len(arr):
            min_child = left_child
        elif arr[left_child] < arr[right_child]:
            min_child = left_child
        else:
            min_child = right_child
        
        arr[index] = arr[min_child]

        index = min_child
        left_child = (2 * index) + 1
        right_child = (2 * index) + 2
    
    # arr.pop(index)
    arr[index] = None
    return min_number

    # while arr[left_child] < arr[index] or arr[right_child] < arr[index]:
    #     if arr[left_child] < arr[index]:
    #         # tmp = arr[index]
    #         arr[index] = arr[left_child]
    #         arr[left_child] = None
    

def heap_peek(arr: list[int]) -> int:
    pass


'''
Implementing a min-heap.

Assumptions
1. The input is an array representation of a binary tree.
2. The array is an in-order traversal of the binary tree.

# Math
Given a node a the i-th index, the left child is at 2i + 1 and the right
child is at 2i + 2.
Given a node at the i-th index, it's parent is located at floor((i - 1) / 2)

'''

arr = [4, None, 9]
heap_push(arr, 2)
# min_value = heap_pop(arr)
print(f"arr: {arr}")
# print(f"min_value: {min_value}")