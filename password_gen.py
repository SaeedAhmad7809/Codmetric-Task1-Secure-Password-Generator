import random
import string

def main():
    print("--- Codmetric Task 1: Secure Password Generator ---")
    
    try:
        # Requirement 1: User-defined length
        length = int(input("[+] Enter the desired password length: "))
        
        if length < 4:
            print("[!] Error: Length must be at least 4 to include all character types.")
            return

        # Requirement 2: Character Types (Upper, Lower, Digits, Special)
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        digits = string.digits
        symbols = string.punctuation

        # Har type ka kam az kam ek character lazmi shamil karna
        password_list = [
            random.choice(upper),
            random.choice(lower),
            random.choice(digits),
            random.choice(symbols)
        ]

        # Baqi ki length ke liye tamam characters ka mix
        all_chars = upper + lower + digits + symbols
        password_list += random.choices(all_chars, k=length - 4)

        # Requirement 3: Randomization
        random.shuffle(password_list)

        # Requirement 4: Display the result
        final_password = "".join(password_list)
        print(f"\n[✔] Your Generated Password: {final_password}")
        print("-" * 40)

    except ValueError:
        print("[X] Error: Please enter a valid number for the length.")

if __name__ == "__main__":
    main()