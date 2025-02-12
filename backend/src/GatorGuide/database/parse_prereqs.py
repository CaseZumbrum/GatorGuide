def parse(pre: str) -> list[list[str]]:
    """parse a prerequisite string from the One.UF API

    Args:
        pre (str): string to be parsed

    Returns:
        list[list[str]]: prerequisites from the string. Those that are grouped together are "or".
        EX: [["COP3502", "COP3504"], ["COT3100"]] is equivalent to (COP3502 or COP3504) and COT3100
    """

    # remove parentheses, slashed, and periods
    pre = pre.replace("(", "").replace(")", "").replace(".", "").replace("/", " ")
    # split words into a list
    words = pre.split()
    prereq_group: list[list[str]] = []

    i = 0
    # iterate through all words
    while i < len(words) - 1:
        # if a word matches the code format
        if (
            words[i].isupper()
            and len(words[i]) == 3
            and len(words[i + 1]) == 4
            and words[i + 1].isnumeric()
        ):
            prereq_group.append([])
            prereq_group[-1].append(words[i] + words[i + 1])
            # attempt to find ORs in the string
            try:
                # while there is an or
                while words[i + 2] == "or":
                    # if the or is followed by a valid course code
                    if (
                        words[i + 3].isupper()
                        and len(words[i + 3]) == 3
                        and len(words[i + 4]) == 4
                        and words[i + 4].isnumeric()
                    ):
                        # add to the group
                        prereq_group[-1].append(words[i + 3] + words[i + 4])
                    i += 3

            except IndexError:
                pass
        i += 1
    return prereq_group


if __name__ == "__main__":
    pass
