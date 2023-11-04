from collections import OrderedDict as od

spain = od([('wins', 0),('loses', 0),('draws', 0),('points', 0),('goalin',0),('goalout',0)])
iran = od([('wins', 0),('loses', 0),('draws', 0),('points', 0),('goalin',0),('goalout',0)])
portugal = od([('wins', 0),('loses', 0),('draws', 0),('points', 0),('goalin',0),('goalout',0)])
morocco = od([('wins', 0),('loses', 0),('draws', 0),('points', 0),('goalin',0),('goalout',0)])


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
        mc["loses"] += 1
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

print("Spain wins:{} , loses:{} , draws:{} , goal diffrence:{} , points:{}".format(spain['wins'], spain['loses'], spain['draws'],
                                                                            spain['goalout']-spain['goalin'], spain['points']))
print("Iran wins:{} , loses:{} , draws:{} , goal diffrence:{} , points:{}".format(iran['wins'], iran['loses'], iran['draws'],
                                                                            iran['goalout']-iran['goalin'], iran['points']))
print("Portugal wins:{} , loses:{} , draws:{} , goal diffrence:{} , points:{}".format(portugal['wins'], portugal['loses'], portugal['draws'],
                                                                            portugal['goalout']-portugal['goalin'], portugal['points']))
print("Morocco wins:{} , loses:{} , draws:{} , goal diffrence:{} , points:{}".format(morocco['wins'], morocco['loses'], morocco['draws'],
                                                                            morocco['goalout']-morocco['goalin'], morocco['points']))