# 1. see source
# 2. run script in <script>..</script>
# 3. see error

p = [70,152,195,284,475,612,791,896,810,850,737,1332,1469,1120,1470,832,1785,2196,1520,1480,1449]
s = ""
for i, c in enumerate(p):
    s += chr(c//(i+1))
print(s)
