n = int(input())
width = []
height = []

for i in range(n):
    a, b = map(int, input().split())
    width.append(a)
    height.append(b)
    
w = max(width) - min(width)
h = max(height) - min(height)

print(w * h)