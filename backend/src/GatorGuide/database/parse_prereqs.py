pre = "Prereq: ACG 3101 with mi…rade of C and FIN 3403"
pre = "COT 3100 or COP 3503 or DSA 3123 and COT 2122"
words = pre.split()
prereq_group: list[list[str]] = []

i = 0
print(words)
while i < len(words) - 1:
    print(i)
    if (
        words[i].isupper()
        and len(words[i]) == 3
        and len(words[i + 1]) == 4
        and words[i + 1].isnumeric()
    ):
        prereq_group.append([])
        prereq_group[-1].append(words[i] + words[i + 1])
        try:
            while words[i + 2] == "or":
                print("hi")
                if (
                    words[i + 3].isupper()
                    and len(words[i + 3]) == 3
                    and len(words[i + 4]) == 4
                    and words[i + 4].isnumeric()
                ):
                    prereq_group[-1].append(words[i + 3] + words[i + 4])
                i += 3

        except IndexError:
            print("out of bounds")
    i += 1
print(prereq_group)
