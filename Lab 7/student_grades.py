def average_marks(marks_csv):
    if not isinstance(marks_csv, str) or not marks_csv.strip():
        return None
    marks = []
    for token in marks_csv.split(','):
        token = token.strip()
        if not token:
            continue
        try:
            marks.append(int(token))
        except ValueError:
            return None
    if not marks:
        return None
    return round(sum(marks) / len(marks), 2)


def parse_srn(srn):
    if not isinstance(srn, str):
        return None
    srn = srn.strip()
    if len(srn) < 10:
        return None
    try:
        year = int(srn[6:8])
    except ValueError:
        return None
    return srn[:4], year, srn[8:10]


def short_name(full_name):
    if not isinstance(full_name, str) or not full_name.strip():
        return None
    parts = full_name.split()
    if len(parts) < 2:
        return None
    first, last = parts[0], parts[-1]
    return first[0].upper() + ". " + last.capitalize()


def main():
    print("==== Running average_marks ====")
    user_input = input("Enter marks as CSV (e.g. 78,85,92): ")
    result = average_marks(user_input)
    print("Average Marks:", result)

    print("\n==== Running parse_srn ====")
    user_input = input("Enter an SRN (e.g. PES1UG23CS123): ")
    result = parse_srn(user_input)
    print("Campus, Year and Dept:", result)

    print("\n==== Running short_name ====")
    user_input = input("Enter first and last name (e.g. ravi kumar): ")
    result = short_name(user_input)
    print("Short Name:", result)


if __name__ == "__main__":
    main()
