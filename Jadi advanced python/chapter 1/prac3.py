from collections import OrderedDict as od

genres = od([('Romance', 0),('Horror', 0),('History', 0),('Comedy', 0),('Adventure', 0),('Action', 0)])

inp_num = int(input())

for i in range(inp_num):
    inp = input()
    inp = inp.split(' ')
    for i in inp[1:4]:
        if i in genres.keys():
            genres[i] += 1


odkeynums = od([(6, 'Action'),(5, 'Adventure'),(4, 'Comedy'),(3, 'History'),(2, 'Horror'),(1, 'Romance')])
odkeys = list(genres.keys())
odvals = list(genres.values())

genre2 = [(odvals[0], 1),(odvals[1], 2),(odvals[2], 3),
          (odvals[3], 4),(odvals[4], 5),(odvals[5], 6)]

genre2.sort()
genre2 = genre2[::-1]

for i in genre2:
    print('{} : {}'.format(odkeynums[i[1]], i[0]))