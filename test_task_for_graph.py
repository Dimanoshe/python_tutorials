def graph_maker(source):
    n = 0
    result = {}
    node = result

    for object in source:
        parent = source[source.index(object)][0]
        print('parent: ', parent)
        child = source[source.index(object)][1]
        print('child: ', child)

        if parent is None:
            result.update({child: {}})
            n += 1

        else:
            node[parent].update({child: {}})
            if n < len(source) - 1 and source[n + 1][0] in result:
                node = result
            elif n < len(source) - 1 and source[n + 1][0] != parent:
                node = node[parent]
            n += 1

    for i in result.items():
        print(i)

if __name__ == '__main__':

    source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
    ]

    graph_maker(source)