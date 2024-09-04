with open('input.txt', 'r') as file:
    f0 = float(file.readline().strip())
    f1 = float(file.readline().strip())
    n = float(file.readline().strip())

elements= []
if n == 0:
    print("your count of step=0")
if n == 1:
    elements.append(f0)
if n >= 2 :
    elements.append(f0)
    elements.append(f1)
def fib(n, f0, f1):
    if n-2>0:
     fn = f0 + f1
     elements.append(fn)
     f0 = f1
     f1 = fn
     fib(n - 1, f0, f1)
fib(n,f0,f1)
with open('output.txt', 'w') as file:
    for element in elements:
     file.write(f"{element}\n")
print("ok")

