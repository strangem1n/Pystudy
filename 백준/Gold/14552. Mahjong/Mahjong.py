import sys
input = sys.stdin.readline

def make_dragon(head, body, head_tile):
    if (head == 1 and body == 3) or (head == 0 and body == 4) or (head == 6 and body == 0):
        rest = []
        for i in range(13):
            if used[i] == 0:
                rest.append(mahjong[i])
        rest.sort()
        if len(rest) == 2:
            if rest[0] + 1 == rest[1]:
                if rest[0] == 1:
                    if tiles[3] < 4:
                        waiting.add(3)
                elif rest[1] == 9:
                    if tiles[7] < 4:
                        waiting.add(7)
                else:
                    if tiles[rest[0]-1] < 4:
                        waiting.add(rest[0]-1)
                    if tiles[rest[1]+1] < 4:
                        waiting.add(rest[1]+1)
            elif rest[0] == rest[1]:
                if rest[0] != head_tile[0]:
                    if tiles[rest[0]] < 4:
                        waiting.add(rest[0])
                    if tiles[head_tile[0]] < 4:
                        waiting.add(head_tile[0])
            elif rest[0] + 2 == rest[1]:
                if tiles[rest[0]+1] < 4:
                    waiting.add(rest[0]+1)
        elif len(rest) == 1:
            if rest[0] not in head_tile and tiles[rest[0]] < 4:
                waiting.add(rest[0])

    else:
        for i in range(13):
            if used[i] == 0:
                tile1 = mahjong[i]
                for j in range(i+1, 13):
                    if used[j] == 0:
                        tile2 = mahjong[j]
                        if tile1 == tile2 and tile1 not in head_tile:
                            used[i] = 1
                            used[j] = 1
                            make_dragon(head+1, body, head_tile+[tile1])
                            used[i] = 0
                            used[j] = 0
                        if head < 2:
                            if (tile1 == tile2) or (tile1+1 == tile2):
                                for k in range(j+1, 13):
                                    if used[k] == 0:
                                        tile3 = mahjong[k]
                                        if (tile1 == tile2 == tile3) or (tile1+2 == tile2+1 == tile3):
                                            used[i] = 1
                                            used[j] = 1
                                            used[k] = 1
                                            make_dragon(head, body+1, head_tile)
                                            used[i] = 0
                                            used[j] = 0
                                            used[k] = 0

mahjong = list(map(int, input().split()))
mahjong.sort()
tiles = {i: 0 for i in range(1, 10)}
for t in mahjong:
    tiles[t] += 1

used = [0] * 13
waiting = set()
make_dragon(0, 0, [])

if len(waiting) == 0:
    print(-1)
else:
    result = list(waiting)
    result.sort()
    print(*result)
