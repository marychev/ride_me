def straight_road(length=20000, step=1000):
    start = {"name": 'Start', "pos": (190, 60)}
    finish = {"name": 'Finish', "pos": (length, 60)}

    map_road = [{"name": 'Lamp', "pos": (i*step, 0)} for i in range(int(length/step)) if i > 0]
    map_road.insert(0, start)
    map_road.insert(len(map_road)-1, finish)
    return map_road
