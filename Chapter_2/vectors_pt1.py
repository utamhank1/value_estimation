def main():
    print("Hello, World: You are running vectors_pt1.py")
    sizes = [1689.0,
             1984.0,
             1581.0,
             1829.0,
             1580.0,
             1621.0,
             2285.0,
             1745.0,
             1747.0,
             998.0,
             2020.0,
             2517.0,
             1835.0
             ]

    for i, value in enumerate(sizes):
        print(f"Updating row {i}")
        sizes[i] = value*.3

    print(sizes)


if __name__ == "__main__":
    main()