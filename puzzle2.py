def solution(args):
    sol = str(args[0]) + ","
    for i in range(1, len(args)):
        if args[i]-args[i-1] != 1:
            sol += str(args[i])
        else:
            while args[i]-args[i-1] == 1:
                i += 1
            sol += "-" + str(args[i]) + ","
    return sol

def main():
    print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))


main()