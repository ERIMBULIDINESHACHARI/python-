def main():
    import sys
    from collections import defaultdict

    # Reading input
    input_data = sys.stdin.read().strip().splitlines()
    N, M = map(int, input_data[0].split())
    
    # Create a friendship graph
    friends = defaultdict(set)
    for i in range(1, M + 1):
        a, b = map(int, input_data[i].split())
        friends[a].add(b)
        friends[b].add(a)
    
    # Read the target rostering value
    K = int(input_data[M + 1])
    
    # Day 1: All employees work from office
    current_attendance = [1] * N  # 1 means WFO, 0 means WFH
    total_rostering_value = N  # Day 1 all N employees are WFO
    days = 1

    while total_rostering_value < K:
        next_attendance = [0] * N
        for employee in range(N):
            friends_in_office = sum(current_attendance[friend] for friend in friends[employee])
            if current_attendance[employee] == 1:  # WFO today
                if friends_in_office == 3:
                    next_attendance[employee] = 1  # Continue WFO
                else:
                    next_attendance[employee] = 0  # WFH next day
            else:  # WFH today
                if friends_in_office < 3:
                    next_attendance[employee] = 1  # WFO next day
                else:
                    next_attendance[employee] = 0  # Continue WFH

        current_attendance = next_attendance
        current_day_count = sum(current_attendance)
        total_rostering_value += current_day_count
        days += 1

    print(days)

# Test Cases
if __name__ == "__main__":
    import io
    import sys

    # Test Case 1
    input_test_1 = """4 5
1 3
3 2
0 3
0 1
2 1
8"""
    sys.stdin = io.StringIO(input_test_1)
    print("Output for Test Case 1:", end=" ")
    main()  # Expected Output: 3

    # Test Case 2
    input_test_2 = """5 7
1 4
0 4
0 1
3 2
3 4
2 0
1 3
15"""
    sys.stdin = io.StringIO(input_test_2)
    print("Output for Test Case 2:", end=" ")
    main()  # Expected Output: 5
