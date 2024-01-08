from collections import namedtuple

Segment = namedtuple('Segment', ['start', 'end'])


def calculate_optimal_points(segments):
    segments_sorted = sorted(segments, key=lambda x: x.start)

    x = segments_sorted[0].end
    points = []

    for s in segments_sorted:
        if s.start > x:
            points.append(x)
            x = s.end
        else:
            x = min(x, s.end)
    points.append(x)
    return points


if __name__ == '__main__':
    user_input_n = int(input())
    user_input_segments = []

    for _ in range(user_input_n):
        segment_values = map(int, input().split())
        user_input_segments.append(Segment(*segment_values))

    result_optimal_points = calculate_optimal_points(user_input_segments)

    print(len(result_optimal_points))
    for p in result_optimal_points:
        print(p, end=' ')
