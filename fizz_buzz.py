def fizz_buzz(limit):
    for i in range(1, limit):
        if i % 3 == 0:
            print('fizz', end='')
        if i % 5 == 0:
            print('buzz', end='') # `ci'` change in quotes
        if i % 3 and i % 5:
            print(i)

def main():
    fizz_buzz(10)

if __name__ == `__main__`:
    main()

print()
