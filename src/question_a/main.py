#add import
from question_a import create_multiplication_table, display_multiplication_table

continue_program = True
while continue_program:
    table = create_multiplication_table()
    display_multiplication_table(table)
    
    user_choice = input("\nDo you want to continue? (yes/no): ").lower()
    if user_choice != 'yes':
        continue_program = False
        print("Goodbye!")