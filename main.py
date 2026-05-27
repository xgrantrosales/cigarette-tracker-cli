from helpers import get_number, get_valid_date
from data_manager import connect_database, create_table, insert_record, fetch_records, update_record, delete_record

# Handles adding new smoking records.
def add_records():

    num_days = get_number("How many days do you want to track?\n", 1)

    for i in range(num_days):

        print(f"\n--- Day {i+1} ---")
        records = fetch_records()
        existing_dates = []

        for record in records:
            existing_dates.append(record[1])

        # Prevent duplicate dates before saving to database.
        while True:

            date = get_valid_date("Please enter date. YYYY-MM-DD\n")

            if date in existing_dates:
                print("Date already exists. Please enter a different date.")
                continue

            break

        daily_limit = get_number("What is your daily target limit?\n", 1)
        smoked = get_number("How many cigarettes have you smoked today?\n", 0)
        # Calculates remaining cigarettes for the day.
        remaining = daily_limit - smoked

        # Determines whether the user stayed within the limit.
        if smoked <= daily_limit:
            status = "Within Limit"
        else:
            status = "Limit Exceeded" 

        insert_record(date, daily_limit, smoked, remaining, status)

    print("Records saved successfully!")

# Displays all saved records and summary statistics.
def view_summary():

    records = fetch_records()

    if len(records) == 0:
        print("No data available.")
        return

    print("\n=== Summary ===")

    for i, record in enumerate(records):
        print(f"\n--- Day {i+1} ---")
        print(f"Date: {record[1]}")
        print(f"Daily Limit: {record[2]}") 
        print(f"Cigarettes Smoked: {record[3]}") 
        print(f"Remaining Cigarettes: {record[4]}") 
        print(f"Status: {record[5]}")
        print()

    total_smoked = 0

    for record in records:
        total_smoked += record[3]
    print(f"Total Cigarettes Smoked: {total_smoked}") 

    total_number_of_days = len(records)
    average = total_smoked / total_number_of_days
    print(f"Average Cigarettes Smoked: {average:.2f}")

    within_limit_count = 0
    exceeded_limit_count = 0

    for record in records:

        if record[5] == "Within Limit":
            within_limit_count += 1
        else:
            exceeded_limit_count += 1

    print(f"Within Limit Count: {within_limit_count}")   
    print(f"Exceeded Limit Count: {exceeded_limit_count}")  

    highest_smoked_record = records[0]
    lowest_smoked_record = records[0]

    for record in records:

        if record[3] > highest_smoked_record[3]:
            highest_smoked_record = record

        if record[3] < lowest_smoked_record[3]:
            lowest_smoked_record = record

    print(f"Highest Smoked Day: {highest_smoked_record[1]} with {highest_smoked_record[3]} cigarettes.")
    print(f"Lowest Smoked Day: {lowest_smoked_record[1]} with {lowest_smoked_record[3]} cigarettes.") 

# Handles editing an existing record.
def edit_records():

    records = fetch_records()

    if len(records) == 0:
        print("No available records to edit.")
        return

    valid_ids = []

    for record in records:
        valid_ids.append(record[0])
        print(f"ID number: {record[0]}. Date: {record[1]} - Cigarettes Smoked: {record[3]}")  

    record_id = get_number("Please enter the record ID that you want to edit.\n", 1)

    # Validates selected ID before updating record.
    if record_id not in valid_ids:
        print("Record ID not found.")
        return

    new_daily_limit = get_number ("What is your new target daily limit?\n", 1)
    new_smoked = get_number("What is your new cigarettes smoked?\n", 0)
    new_remaining = new_daily_limit - new_smoked

    if new_smoked <= new_daily_limit:
        new_status = "Within Limit"
    else:
        new_status = "Limit Exceeded"

    update_record(record_id, new_daily_limit, new_smoked, new_remaining, new_status)    
    print("Record edited successfully!")   

# Handles deleting an existing record.
def delete_records():

    records = fetch_records()

    if len(records) == 0:
        print("No available records to delete.")
        return

    valid_ids = []

    for record in records:
        valid_ids.append(record[0])
        print(f"ID number: {record[0]}. Date: {record[1]} - Cigarettes Smoked: {record[3]}")

    record_id = get_number("Please enter the record ID that you want to delete.\n", 1)

    # Validates selected ID before deleting record.
    if record_id not in valid_ids:
        print("Record ID not found.")
        return

    delete_record(record_id)  
    print(f"ID number {record_id} deleted successfully!")

# Main application loop and menu navigation.
def main():

    connection = connect_database()
    create_table(connection)

    while True:

        print("\n=== Cigarette Tracker Menu ===")
        print("1. Add Record")
        print("2. View Summary")
        print("3. Edit Record")
        print("4. Delete Record")
        print("5. Exit")

        user_choice = get_number("Please enter the number of your choice.\n", 1, 5)

        if user_choice == 1:
            add_records()

        elif user_choice == 2:
            view_summary()

        elif user_choice == 3:
            edit_records()

        elif user_choice == 4:
            delete_records()

        elif user_choice == 5:
            print("Goodbye!")
            break

# Starts the app only when main.py is executed directly.
if __name__ == "__main__":
    main()                                                                   


