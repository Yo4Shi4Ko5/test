f = open('input.txt', 'r')
data = f.read().split("\n")
f.close()

target_num = int(data[-2])
data = data[:-2]

def num_get(s):
    return int(s.split(":")[0])

def str_get(s):
    return s.split(":")[1]

num_data = list(map(num_get, data))
str_data = list(map(str_get, data))

idx = list(range(len(num_data)))
sort_idx = sorted(idx, key=lambda i: num_data[i])

ans_str = ""

for i in sort_idx:
    num = num_data[i]
    s = str_data[i]
    
    if not (target_num % num):
        ans_str += s

print(ans_str if ans_str else target_num)