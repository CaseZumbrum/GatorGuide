def parse(pre: str):
    pre = pre.replace("(", "").replace(")", "").replace(".", "").replace("/", " ")
    words = pre.split()
    prereq_group: list[list[str]] = []

    i = 0
    while i < len(words) - 1:
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
                    if (
                        words[i + 3].isupper()
                        and len(words[i + 3]) == 3
                        and len(words[i + 4]) == 4
                        and words[i + 4].isnumeric()
                    ):
                        prereq_group[-1].append(words[i + 3] + words[i + 4])
                    i += 3

            except IndexError:
                pass
        i += 1
    return prereq_group


if __name__ == "__main__":
    pass
