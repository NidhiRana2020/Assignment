def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence[:n]

def main():
    try:
        n = int(input("Enter the number of terms for the Fibonacci sequence: "))
        
        if n <= 0:
            print("Please enter a positive integer for the number of terms.")
        else:
            fibonacci_sequence = generate_fibonacci(n)
            print(f"Fibonacci sequence with {n} terms: {fibonacci_sequence}")

    except ValueError:
        print("Please enter a valid integer for the number of terms.")

if __name__ == "__main__":
    main()
