# Author: Phillip Hampton Ewing, Jr.
# Email: phewing@alum.mit.edu
# Website: www.phillipewing.com

def modulor(n):
    red_sequence, blue_sequence = [0, 1], [0, 2]
    for i in range(n//2 + 2):
        red_sequence.append(red_sequence[-1] + red_sequence[-2])
        blue_sequence.append(blue_sequence[-1] + blue_sequence[-2])
    if n % 2 == 0:
        return sorted(list(set(red_sequence[1:] + blue_sequence[1:-2])))[:-1]
    else:
        return sorted(list(set(red_sequence[1:] + blue_sequence[1:-1])))[:-1]

if __name__ == "__main__":
    scale = modulor(32)
    print(scale, len(scale))