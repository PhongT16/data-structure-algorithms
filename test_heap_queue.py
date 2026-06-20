import pytest
from heap_queue import myHeapQueue


def is_min_heap(arr):
    for i in range(len(arr)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(arr) and arr[left] < arr[i]:
            return False
        if right < len(arr) and arr[right] < arr[i]:
            return False
    return True


class TestHeapify:
    def test_basic(self):
        arr = [10, 7, 3, 5, 12, 4, 0, 8, 15]
        myHeapQueue.heapify(arr)
        assert is_min_heap(arr)

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        myHeapQueue.heapify(arr)
        assert is_min_heap(arr)

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        myHeapQueue.heapify(arr)
        assert is_min_heap(arr)

    def test_duplicates(self):
        arr = [3, 3, 3, 1, 1]
        myHeapQueue.heapify(arr)
        assert is_min_heap(arr)

    def test_single_element(self):
        arr = [42]
        myHeapQueue.heapify(arr)
        assert arr == [42]

    def test_two_elements(self):
        arr = [5, 1]
        myHeapQueue.heapify(arr)
        assert is_min_heap(arr)

    def test_min_is_at_root(self):
        arr = [10, 7, 3, 5, 12, 4, 0, 8, 15]
        myHeapQueue.heapify(arr)
        assert arr[0] == min([10, 7, 3, 5, 12, 4, 0, 8, 15])

    def test_negative_numbers(self):
        arr = [-3, 5, -1, 0, 8, -7]
        myHeapQueue.heapify(arr)
        assert is_min_heap(arr)


class TestHeappush:
    def test_push_smaller_than_root(self):
        arr = [10, 7, 3, 5, 12, 4, 0, 8, 15]
        myHeapQueue.heapify(arr)
        myHeapQueue.heapppush(arr, -1)
        assert is_min_heap(arr)
        assert arr[0] == -1

    def test_push_larger_than_all(self):
        arr = [1, 3, 2]
        myHeapQueue.heapify(arr)
        myHeapQueue.heapppush(arr, 100)
        assert is_min_heap(arr)
        assert 100 in arr

    def test_push_into_empty(self):
        arr = []
        myHeapQueue.heapppush(arr, 5)
        assert arr == [5]

    def test_push_preserves_min_at_root(self):
        arr = [1, 3, 2]
        myHeapQueue.heapify(arr)
        myHeapQueue.heapppush(arr, 0)
        assert arr[0] == 0

    def test_multiple_pushes(self):
        arr = []
        for val in [5, 3, 8, 1, 4]:
            myHeapQueue.heapppush(arr, val)
        assert is_min_heap(arr)
        assert arr[0] == 1

    def test_push_none_raises(self):
        with pytest.raises((TypeError, ValueError)):
            myHeapQueue.heapppush(None, 5)


class TestHeappop:
    def test_returns_minimum(self):
        arr = [10, 7, 3, 5, 12, 4, 0, 8, 15]
        myHeapQueue.heapify(arr)
        result = myHeapQueue.heappop(arr)
        assert result == 0

    def test_heap_property_after_pop(self):
        arr = [10, 7, 3, 5, 12, 4, 0, 8, 15]
        myHeapQueue.heapify(arr)
        myHeapQueue.heappop(arr)
        assert is_min_heap(arr)

    def test_size_decreases(self):
        arr = [1, 2, 3]
        myHeapQueue.heapify(arr)
        myHeapQueue.heappop(arr)
        assert len(arr) == 2

    def test_pop_all_elements_sorted(self):
        original = [10, 7, 3, 5, 12, 4, 0, 8, 15]
        arr = original[:]
        myHeapQueue.heapify(arr)
        popped = []
        while arr:
            popped.append(myHeapQueue.heappop(arr))
        assert popped == sorted(original)

    def test_single_element(self):
        arr = [42]
        result = myHeapQueue.heappop(arr)
        assert result == 42
        assert arr == []

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            myHeapQueue.heappop([])

    def test_no_none_left_in_array(self):
        arr = [5, 3, 8, 1, 4]
        myHeapQueue.heapify(arr)
        myHeapQueue.heappop(arr)
        assert None not in arr


class TestHeappeek:
    def test_returns_min(self):
        arr = [1, 3, 2]
        myHeapQueue.heapify(arr)
        assert myHeapQueue.heappeek(arr) == 1

    def test_does_not_modify_array(self):
        arr = [1, 3, 2]
        myHeapQueue.heapify(arr)
        before = arr[:]
        myHeapQueue.heappeek(arr)
        assert arr == before

    def test_after_push(self):
        arr = [3, 5, 4]
        myHeapQueue.heapify(arr)
        myHeapQueue.heapppush(arr, 1)
        assert myHeapQueue.heappeek(arr) == 1
