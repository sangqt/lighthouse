user_boxes = {'weight': [4, 2, 18, 21, 14, 13],
              'box_name': ['box1', 'box2', 'box3', 'box4', 'box5', 'box6']
              }


def my_function(wlist, nlist):
    we = sorted(wlist)
    # print(wlist)
    # print(we)
    open_boxes = []
    for i in we:
        for t in range(len(wlist)):
            # print(wlist[t])
            if wlist[t] == i:
                open_boxes.append(nlist[t])

    print(open_boxes)


my_function(user_boxes['weight'], user_boxes['box_name'])
