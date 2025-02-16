import sys

def parse_csv(content):
    rows = []
    current_row = []
    inside_quotes = False
    field = ""
    
    for char in content:
        if char == '"':
            inside_quotes = not inside_quotes
        elif char == '\n' and not inside_quotes:
            current_row.append(field)
            rows.append(current_row)
            current_row = []
            field = ""
        elif char == ';' and not inside_quotes:
            current_row.append(field)
            field = ""
        else:
            field += char
    
    if field:
        current_row.append(field)
    if current_row:
        rows.append(current_row)
    
    return rows[1:]

def sorted_composers(data):
    return sorted(set(row[4] for row in data))

def distribution_by_period(data):
    distribution = {}
    
    for row in data:
        period = row[3]
        distribution[period] = distribution.get(period, 0) + 1
    
    return distribution

def titles_by_period(data):
    titles_by_period = {}
    
    for row in data:
        period, title = row[3], row[0]
        titles_by_period.setdefault(period, []).append(title)
    
    for period in titles_by_period:
        titles_by_period[period].sort()
    
    return titles_by_period


def main():
    if len(sys.argv) != 2:
        file = "obras.csv"
    else:
        file = sys.argv[1]

    with open(file, encoding="utf-8") as f:
        content = f.read()

    data = parse_csv(content)

    composers = sorted_composers(data)
    distribution = distribution_by_period(data)
    titles = titles_by_period(data)

    print("== Compositores ordenados ==")
    for composer in composers:
        print(composer)

    print("== Distribuição por período ==")
    for period, count in distribution.items():
        print(f"{period}: {count}")

    print("== Títulos por período ==")
    for period, titles in titles.items():
        print(f"{period}:")
        for title in titles:
            print(f"  {title}")

if __name__ == "__main__":
    main()