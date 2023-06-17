data = []
mod_data = []

for i in range(10):
  data.append(int(input()))
  mod_data.append(data[i] % 42)

print(len(set(mod_data)))