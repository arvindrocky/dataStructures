import time

class Solution:
    def generate_sub_arrays(self, main_array: list, from_len: int, to_len: int) -> None:
        for ele, index in enumerate(main_array):
            # print(main_array[index-1:index])
            for y, j in enumerate(main_array[index:]):
                sub_array = main_array[index-1:j]
                if from_len <= len(sub_array) <= to_len:
                    #print(sub_array)
                    pass

    def generate_sub_array_with_len(self, main_array: list, from_len: int, to_len: int) -> None:
        for ele, i in enumerate(main_array):
            a = from_len
            while a <= to_len and (i - 1 + a) <= len(main_array):
                #print(main_array[i-1:(i-1+a)])
                a += 1


sol = Solution()
input = list(range(1, 10001))
from_len = 2
to_len = 4

# start_time = time.process_time()
# sol.generate_sub_arrays(input, from_len, to_len)
# end_time = time.process_time()


start_time1 = time.process_time()
sol.generate_sub_array_with_len(input, from_len, to_len)
end_time1 = time.process_time()

# print(end_time - start_time)
print(end_time1 - start_time1)
