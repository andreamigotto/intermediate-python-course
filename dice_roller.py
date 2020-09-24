import random

def main():
  n_rolls = 2
  for i in range(0,n_rolls):
    roll = random.randint(1,6)
    print(f'You rolled a {roll}')


if __name__ == "__main__":
  main()
