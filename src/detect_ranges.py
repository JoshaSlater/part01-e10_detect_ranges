#!/usr/bin/env python3

def detect_ranges(L):
    L2 = sorted(L)
    L3 = []
    inrange = False
    start = 1
    end = 1
    
    for i in range(1, len(L2)):
        if L2[i] != L2[i - 1] + 1:
            if inrange == False:
                L3.append(L2[i-1])
            elif inrange:
                    range2 = (start, end + 1)
                    L3.append(range2)
                    inrange = False
        else:
            if inrange:
                    end = L2[i]
                    
            elif inrange == False:
                    inrange = True
                    start = L2[i-1]
    return(L3)


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()
