#add import
from question_c import get_most_likely_ancestor_consensus

def main():
    continue_program = True
    
    while continue_program:
        # Get and validate DNA string 1
        while True:
            dna_string1 = input("Enter a DNA string (greater than 8 and less than or equal to 16 characters): ").strip()
            if 8 < len(dna_string1) <= 16:
                break
            else:
                print(f"Invalid input. DNA string must be between 9 and 16 characters. Your input has {len(dna_string1)} characters.")
        
        # Get and validate DNA string 2
        while True:
            dna_string2 = input("Enter a DNA substring (exactly 4 characters): ").strip()
            if len(dna_string2) == 4:
                break
            else:
                print(f"Invalid input. DNA substring must be exactly 4 characters. Your input has {len(dna_string2)} characters.")
        
        # Call the function and display results
        results = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        
        if results:
            print(f"\nPositions found: {' '.join(map(str, results))}")
        else:
            print(f"\nNo occurrences of '{dna_string2}' found in '{dna_string1}'")
        
        # Ask if user wants to continue
        user_choice = input("\nDo you want to continue? (yes/no): ").lower().strip()
        if user_choice != 'yes':
            continue_program = False
            print("Goodbye!")

if __name__ == "__main__":
    main()