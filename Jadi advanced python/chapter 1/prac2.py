from collections import OrderedDict as od

spain = od([('Spain', ''),('wins', 0),('loses', 0),('draws', 0),('points', 0),('goalin',0),('goalout',0),('gdifferece', 0)])
iran = od([('Iran', ''),('wins', 0),('loses', 0),('draws', 0),('points', 0),('goalin',0),('goalout',0),('gdifferece', 0)])
portugal = od([('Portugal', ''),('wins', 0),('loses', 0),('draws', 0),('points', 0),('goalin',0),('goalout',0),('gdifferece', 0)])
morocco = od([('Morocco', ''),('wins', 0),('loses', 0),('draws', 0),('points', 0),('goalin',0),('goalout',0),('gdifferece', 0)])


def stat_1(x):
    ir = int(x[0])
    sp = int(x[1])
    if sp>ir:
        spain['wins'] += 1
        spain['points'] += 3
        iran["loses"] += 1
    elif sp==ir:
        spain['draws'] += 1
        spain['points'] += 1
        iran['draws'] += 1
        iran['points'] += 1
    elif sp<ir:
        iran['wins'] += 1
        iran['points'] += 3
        spain["loses"] += 1
    spain['goalout'] += sp
    spain['goalin'] += ir
    iran['goalout'] += ir
    iran['goalin'] += sp
    
def stat_2(x):
    ir = int(x[0])
    pt = int(x[1])
    if pt>ir:
        portugal['wins'] += 1
        portugal['points'] += 3
        iran["loses"] += 1
    elif pt==ir:
        portugal['draws'] += 1
        portugal['points'] += 1
        iran['draws'] += 1
        iran['points'] += 1
    elif pt<ir:
        iran['wins'] += 1
        iran['points'] += 3
        portugal["loses"] += 1
    portugal['goalout'] += pt
    portugal['goalin'] += ir
    iran['goalout'] += ir
    iran['goalin'] += pt


def stat_3(x):
    ir = int(x[0])
    mc = int(x[1])
    if mc>ir:
        morocco['wins'] += 1
        morocco['points'] += 3
        iran["loses"] += 1
    elif mc==ir:
        morocco['draws'] += 1
        morocco['points'] += 1
        iran['draws'] += 1
        iran['points'] += 1
    elif mc<ir:
        iran['wins'] += 1
        iran['points'] += 3
        morocco["loses"] += 1
    morocco['goalout'] += mc
    morocco['goalin'] += ir
    iran['goalout'] += ir
    iran['goalin'] += mc



def stat_4(x):
    sp = int(x[0])
    pt = int(x[1])
    if sp>pt:
        spain['wins'] += 1
        spain['points'] += 3
        portugal["loses"] += 1
    elif sp==pt:
        spain['draws'] += 1
        spain['points'] += 1
        portugal['draws'] += 1
        portugal['points'] += 1
    elif sp<pt:
        portugal['wins'] += 1
        portugal['points'] += 3
        spain["loses"] += 1
    spain['goalout'] += sp
    spain['goalin'] += pt
    portugal['goalout'] += pt
    portugal['goalin'] += sp


def stat_5(x):
    sp = int(x[0])
    mc = int(x[1])
    if sp>mc:
        spain['wins'] += 1
        spain['points'] += 3
        morocco["loses"] += 1
    elif sp==mc:
        spain['draws'] += 1
        spain['points'] += 1
        morocco['draws'] += 1
        morocco['points'] += 1
    elif sp<mc:
        morocco['wins'] += 1
        morocco['points'] += 3
        spain["loses"] += 1
    spain['goalout'] += sp
    spain['goalin'] += mc
    morocco['goalout'] += mc
    morocco['goalin'] += sp


def stat_6(x):
    pt = int(x[0])
    mc = int(x[1])
    if mc>pt:
        morocco['wins'] += 1
        morocco['points'] += 3
        portugal["loses"] += 1
    elif mc==pt:
        morocco['draws'] += 1
        morocco['points'] += 1
        portugal['draws'] += 1
        portugal['points'] += 1
    elif mc<pt:
        portugal['wins'] += 1
        portugal['points'] += 3
        morocco["loses"] += 1
    morocco['goalout'] += mc
    morocco['goalin'] += pt
    portugal['goalout'] += pt
    portugal['goalin'] += mc

input_data = []
for i in range(6):
    x = input()
    x = x.split('-')
    input_data.append((x[0], x[1]))

stat_1(input_data[0])
stat_2(input_data[1])
stat_3(input_data[2])
stat_4(input_data[3])
stat_5(input_data[4])
stat_6(input_data[5])

spain['gdifferece'] = spain['goalout'] - spain['goalin']
iran['gdifferece'] = iran['goalout'] - iran['goalin']
portugal['gdifferece'] = portugal['goalout'] - portugal['goalin']
morocco['gdifferece'] = morocco['goalout'] - morocco['goalin']

biglist = []
biglist.append(list(iran.items()))
biglist.append(list(morocco.items()))
biglist.append(list(portugal.items()))
biglist.append(list(spain.items()))

biglist.sort()
biglist.sort(key = lambda x:(x[4], x[1]), reverse=True)

print("{} wins:{} , loses:{} , draws:{} , goal difference:{} , points:{}".format(biglist[0][0][0], biglist[0][1][1], biglist[0][2][1], biglist[0][3][1], biglist[0][7][1], biglist[0][4][1]))
print("{} wins:{} , loses:{} , draws:{} , goal difference:{} , points:{}".format(biglist[1][0][0], biglist[1][1][1], biglist[1][2][1], biglist[1][3][1], biglist[1][7][1], biglist[1][4][1]))
print("{} wins:{} , loses:{} , draws:{} , goal difference:{} , points:{}".format(biglist[2][0][0], biglist[2][1][1], biglist[2][2][1], biglist[2][3][1], biglist[2][7][1], biglist[2][4][1]))
print("{} wins:{} , loses:{} , draws:{} , goal difference:{} , points:{}".format(biglist[3][0][0], biglist[3][1][1], biglist[3][2][1], biglist[3][3][1], biglist[3][7][1], biglist[3][4][1]))
