def swapFS(DanNoemIkHetGeenlist):
    if len(DanNoemIkHetGeenlist) > 1:
        DanNoemIkHetGeenlist[0],DanNoemIkHetGeenlist[1] = DanNoemIkHetGeenlist[1],DanNoemIkHetGeenlist[0]

lijst1 = [2,5,4,2,1,6,99]
swapFS(lijst1)

print(lijst1)