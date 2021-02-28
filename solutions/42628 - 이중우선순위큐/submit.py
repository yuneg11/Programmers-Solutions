from heapq import heappush as push, heappop as pop

def solution(o, i=0, sh=set(), nh=[], xh=[]):
    for e in o:
        if (v := e.split(" "))[0] == "I":
            push(nh, (int(v[1]), i))
            push(xh, (-int(v[1]), i))
            sh.add(i)
            i += 1
        elif sh:
            m = xh if v[1] == "1" else nh
            while (k := pop(m))[1] not in sh: pass
            sh.remove(k[1])

    if sh:
        while (mx := pop(xh))[1] not in sh: pass
        while (mn := pop(nh))[1] not in sh: pass

    return [-mx[0] if sh else 0, mn[0] if sh else 0]
