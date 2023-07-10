#!/usr/bin/python3
'''
inheritance learning file
'''


class MyList(list):
    def print_sorted(self):
        lsi = self[:]
        n = len(lsi)
        for i in range(n):
            for j in range(0, n-i-1):
                if lsi[j] > lsi[j+1]:
                    lsi[j], lsi[j+1] = lsi[j+1], lsi[j]
        print(lsi)
