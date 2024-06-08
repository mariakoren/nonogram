import time
from main import nonogram_ga
from main2 import nonogram_ga2
# nonograms example

nonogram_1_1 = [
    [[1,1,1], [3], [5], [3], [1,1,1]],
    [[1,1,1], [3], [5], [3], [1,1,1]]
    ]
nonogram_1_2 = [
    [[2], [1, 1], [1, 1], [1, 1], [2]],
    [[1,1], [1, 1,1], [1, 1], [1,1], [1]]
]

nonogram_1_3 = [
    [[1], [2, 1], [5], [2, 1], [1]],
    [[1], [3], [5], [3], [1]]
]

nonogram_2_1 = [
    [[0], [2], [3], [1], [1, 2, 2], [1, 2, 2], [1, 2], [6], [4], [0]],
    [[6], [2, 2], [2, 2], [2], [3], [4], [2], [0], [2], [2]]
]

nonogram_2_2 = [
    [[1], [4, 2], [1, 2], [6, 1], [1, 2, 1], [5, 1, 1], [1, 2, 1, 1], [3, 1, 2], [1, 5], [2]],
    [[6], [1, 1, 1, 1], [2, 1, 2], [1, 1, 2, 1], [1, 1, 4], [1, 2, 1], [8], [1, 1], [1, 4], [2]]
]

nonogram_2_3 = [
    [[3,1],[5,2],[3,2,1],[4,1,1],[10],[1,7],[3,1,1,1],[3,1,1],[4,1],[2,2]],
    [[6],[4,3],[5,4],[2,3,2],[3,5],[5],[3],[2],[1,2,1],[10]]
]

# nonogram_2_3 = [
#     [[6], [7], [8], [9], [5, 3], [5, 3], [9], [8], [7], [6]],
#     [[2], [4], [6], [8], [10], [4, 4], [4, 4], [10], [10], [10]]
# ]


nonogram_3_1 = [
    [[1,2,2], [2,2,4,2], [2,3,6], [2,2,1,2], [3,1], [1,3], [1,1,7],[7,2],[1,10], [5,1], [5,2], [5, 1], [3,9,1],[2,3,1],[5]],
    [[4,1,1],[3,1],[5],[1,1,1,3],[4,5],[4,8],[7],[1,2,1],[2,4,1],[3,4,1],[8,5],[1,5,3],[1,1,1,3],[4,3,1],[4,2,3]]
]

start_time1_1= time.time()
res1_1 = nonogram_ga2(nonogram_1_1, "1_1")
end_time1_1 = time.time()
t1_1= end_time1_1- start_time1_1

start_time1_2 = time.time()
res1_2 =nonogram_ga(nonogram_1_2, "1_2")
end_time1_2 = time.time()
t1_2 = end_time1_2 - start_time1_2

start_time1_3 = time.time()
res1_3 =nonogram_ga(nonogram_1_3, "1_3")
end_time1_3 = time.time()
t1_3 = end_time1_3 - start_time1_2


start_time2_1 = time.time()
res2_1 =nonogram_ga(nonogram_2_1, "2_1")
end_time2_1 = time.time()
t2_1 = end_time2_1 - start_time2_1

start_time2_2 = time.time()
res2_2 =nonogram_ga(nonogram_2_2, "2_2")
end_time2_2 = time.time()
t2_2 = end_time2_2 - start_time2_2

start_time2_3 = time.time()
res2_3 =nonogram_ga(nonogram_2_3, "2_3")
end_time2_3 = time.time()
t2_3 = end_time2_3 - start_time2_3


start_time3_1 = time.time()
res3_1 =nonogram_ga(nonogram_3_1, "3_1")
end_time3_1 = time.time()
t3_1 = end_time3_1 - start_time3_1

print("statistics:")
print("5x5")
print(f"accuracy: {res1_1}, {res1_2}, {res1_3}; average {(res1_1+res1_2+res1_3)/3}")
print(f"time: {t1_1}, {t1_2}, {t1_3}; average {(t1_1+t1_2+t1_3)/3}")
print()
print("10x10")
print(f"accuracy: {res2_1}, {res2_2}, {res2_3}; average {(res2_1+res2_2+res2_3)/3}")
print(f"time: {t2_1}, {21_2}, {t2_3}; average {(t2_1+t2_2+t2_3)/3}")
print()
print("15x15")
print(f"accuracy: {res3_1}")
print(f"time: {t3_1}")
