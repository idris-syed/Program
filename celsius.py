c, f=map(float, input().split())
c_to_f=(c*9/5) + 32
f_to_c = (f - 32)*5/9
print(f"{c} C = {c_to_f} F ")
print(f"{f} F = {round(f_to_c,2)}c")