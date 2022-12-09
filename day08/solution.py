grid = {}
grid_score = {}
def input_reader(filename):
    return [ list(line.strip()) for line in open(filename).readlines()]

maxsize = {}


def is_hidden(x, y):
    hidden_left = any(list(map(lambda i:  grid[(x,y)] <= grid[(i,y)], list(range(0, x)))))
    if not hidden_left:
        return False
    hidden_right = any(list(map(lambda i:  grid[(x,y)] <= grid[(i,y)], list(range(x+1, maxsize['x'])))))
    if not hidden_right:
        return False
    hidden_top = any(list(map(lambda i:  grid[(x,y)] <= grid[(x,i)], list(range(0, y)))))
    if not hidden_top:
        return False
    hidden_bottom = any(list(map(lambda i:  grid[(x,y)] <= grid[(x,i)], list(range(y+1, maxsize['y'])))))
    if not hidden_bottom:
        return False
    return True

def scenic_score(x, y):
    leftfree = 1
    for i in list(range(x-1, 0, -1)): # Start left from the current one, go back to 0
        if grid[(i,y)] < grid[(x,y)]:
            leftfree += 1
        else:
            break

    rightfree = 1
    for i in list(range(x+1, maxsize['x'])): 
        if grid[(i,y)] < grid[(x,y)]:
            rightfree += 1
        else:
            break

    topfree = 1
    for j in list(range(y-1, 0, -1)): 
        if grid[(x,j)] < grid[(x,y)]:
            topfree += 1
        else:
            break

    bottomfree = 1
    for j in list(range(y+1, maxsize['y'])): 
        if grid[(x,j)] < grid[(x,y)]:
            bottomfree += 1
        else:
            break

    return leftfree*rightfree*topfree*bottomfree

def main(test=True):
    data = input_reader("test.txt" if test else "input.txt")
    for y, line in enumerate(data):
        for x, val in enumerate(line):
            grid.update({
                (x, y): val
            })
    maxsize.update({
        "x": x,
        "y": y
    })
    count = 0
    for i in list(range(1, maxsize['x'])):
        for j in list(range(1, maxsize['y'])):
            if is_hidden(i,j):
                count += 1

            grid_score.update({(i,j): scenic_score(i,j)})
    print(f"Part one: {len(grid)-count}")
    print(f"Part two: {max(grid_score.values())}")
if __name__ == '__main__':
    main(test=False)