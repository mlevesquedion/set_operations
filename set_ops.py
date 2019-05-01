def _merge(S1, S2, operations):
    S1, S2 = sorted(S1), sorted(S2)
    i = j = 0
    result = []
    while i < len(S1) and j < len(S2):
        v1, v2 = S1[i], S2[j]
        if v1 == v2:
            operations['eq'](v1, v2, result)
            i += 1
            j += 1
        elif v1 < v2:
            operations['lt'](v1, v2, result)
            i += 1
        else:
            operations['gt'](v1, v2, result)
            j += 1
    for k in range(i, len(S1)):
        operations['rem_first'](S1[k], result)
    for k in range(j, len(S2)):
        operations['rem_second'](S2[k], result)
    return result


def second(_a, b):
    return b


def third(_a, _b, c):
    return c


def append_v(v, res):
    return res.append(v)


def append_first(a, b, res):
    return append_v(a, res)


def append_second(a, b, res):
    return append_v(b, res)


def intersection(S1, S2):
    return _merge(S1, S2,
                  {
                      'eq': append_first,
                      'lt': third,
                      'gt': third,
                      'rem_first': second,
                      'rem_second': second,
                  })


def union(S1, S2):
    return _merge(S1, S2,
                  {
                      'eq': append_first,
                      'lt': append_first,
                      'gt': append_second,
                      'rem_first': append_v,
                      'rem_second': append_v,
                  })


def difference(S1, S2):
    return _merge(S1, S2,
                  {
                      'eq': third,
                      'lt': append_first,
                      'gt': third,
                      'rem_first': append_v,
                      'rem_second': second
                  })


def symmetric_difference(S1, S2):
    return _merge(S1, S2, {
        'eq': third,
        'lt': append_first,
        'gt': append_second,
        'rem_first': append_v,
        'rem_second': append_v
    })
