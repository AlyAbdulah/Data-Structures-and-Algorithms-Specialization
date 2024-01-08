def count_segments(starts, ends, points):
    cnt = [0] * len(points)
    points_num = [i for _, i in sorted(zip(points, range(len(points))))]

    full_points = [(p, 1) for p in points]
    full_points.extend([(s, 0) for s in starts])
    full_points.extend([(e, 2) for e in ends])

    full_points.sort()

    num_open_segments = 0
    i = 0
    for val, p_type in full_points:
        if p_type == 0:
            num_open_segments += 1
        elif p_type == 2:
            num_open_segments -= 1
        else:
            cnt[points_num[i]] = num_open_segments
            i += 1
    return cnt


if __name__ == '__main__':
    n_segments, n_points = map(int, input().split())
    segments = [tuple(map(int, input().split())) for _ in range(n_segments)]
    points = list(map(int, input().split()))

    starts, ends = zip(*segments)

    cnt = count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
