t = int(input())

def recursive(idx, calc, results):
    # basis part
    if idx == n:
        if eval(calc.replace(" ","")) == 0:
            results.append(calc)
        return

    # inductive part
    recursive(idx + 1, calc+" "+str(idx + 1), results)
    recursive(idx + 1, calc+"+"+str(idx + 1), results)
    recursive(idx + 1, calc+"-"+str(idx + 1), results)

for tc in range(t):
    n = int(input())
    results = []
    recursive(1,"1",results)
    for result in results:
        print(result)
    print()
