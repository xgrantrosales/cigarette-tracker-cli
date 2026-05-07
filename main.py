from helpers import get_number, get_valid_date
from data_manager import load_records, save_records

def add_records(records):

    num_days = get_number("How many days do you want to track?\n", 1)

    for i in range(num_days):

        print(f"\n--- Day {i+1} ---")

        date = get_valid_date("Please enter date. YYYY-MM-DD\n")
        daily_limit = get_number("What is your target daily limit?\n", 1)
        smoked = get_number("How many cigarettes have you smoked today?\n", 0)
        remaining = daily_limit - smoked

        if smoked <= daily_limit:
            status = "Within Limit"
        else:
            status = "Limit Exceeded"

        record = {
            "date": date,
            "daily_limit": daily_limit,
            "smoked": smoked,
            "remaining": remaining,
            "status": status
        }   

        records.append(record)

    save_records(records)
    print("Records saved successfully!")

def view_summary(records):

    if len(records) == 0:
        print("No available data.")
        return

    print("\n=== Summary ===")

    for i, record in enumerate(records):
        print(f"\n--- Day {i+1} ---")
        print(f"Date: {record['date']}")
        print(f"Daily Limit: {record['daily_limit']}")
        print(f"Cigarettes Smoked: {record['smoked']}")
        print(f"Remaining Cigarettes: {record['remaining']}")
        print(f"Status: {record['status']}")
        print()

    total_smoked = 0

    for record in records:
        total_smoked += record["smoked"]
    print(f"Total Cigarettes Smoked: {total_smoked}")

    total_number_of_days = len(records)
    average = total_smoked / total_number_of_days
    print(f"Average Smoked Cigarettes: {average:.2f}")

    within_limit_count = 0
    exceeded_limit_count = 0

    for record in records:
        if record["status"] == "Within Limit":
            within_limit_count += 1
        else:
            exceeded_limit_count += 1

    print(f"Within Limit Count: {within_limit_count}")   
    print(f"Exceeded Limit Count: {exceeded_limit_count}") 

    highest_smoked_record = records[0]
    lowest_smoked_record = records[0]

    for record in records:

        if record["smoked"] > highest_smoked_record["smoked"]:
            highest_smoked_record = record

        if record["smoked"] < lowest_smoked_record["smoked"]:
            lowest_smoked_record = record

    print(f"Highest Smoked Day: {highest_smoked_record['date']} with {highest_smoked_record['smoked']} cigarettes.") 
    print(f"Lowest Smoked Day: {lowest_smoked_record['date']} with {lowest_smoked_record['smoked']} cigarettes.")

def edit_records(records):

    if len(records) == 0:
        print("No available records to edit.")
        return
    
    for i, record in enumerate(records):
        print(f"{i+1}. Date: {record['date']} - Cigarettes Smoked: {record['smoked']}")

    user_choice = get_number("Please enter the number of the record that you want to edit.\n", 1, len(records))

    selected_index = user_choice - 1
    selected_record = records[selected_index]

    new_daily_limit = get_number("What is your new target daily limit?\n", 1)
    new_smoked = get_number("What is your new number of smoked cigarettes?\n", 0) 
    new_remaining = new_daily_limit - new_smoked

    if new_smoked <= new_remaining:
        new_status = "Within Limit"
    else:
        new_status = "Limit Exceeded"

    selected_record["daily_limit"] = new_daily_limit
    selected_record["smoked"] = new_smoked
    selected_record["remaining"] = new_remaining
    selected_record["status"] = new_status

    save_records(records)  
    print("Record edited successfully!")    

def delete_records(records):

    if len(records) == 0:
        print("No available records to delete.")
        return

    for i, record in enumerate(records):
        print(f"{i+1}. Date: {record['date']} - Cigarettes Smoked: {record['smoked']}")

    user_choice = get_number("Please enter the number of the record that you want to delete.\n", 1, len(records))

    selected_index = user_choice - 1
    removed_record = records.pop(selected_index)    

    save_records(records)
    print(f"Record for {removed_record['date']} deleted successfully!")

def main():

    records = load_records()

    while True:

        print("\n=== Cigarette Tracker Menu ===")
        print("1. Add Record")
        print("2. View Summary")
        print("3. Edit Record")
        print("4. Delete Record")
        print("5. Exit")

        user_choice = get_number("Please enter the number of your choice.\n", 1, 5)

        if user_choice == 1:
            add_records(records)

        elif user_choice == 2:
            view_summary(records)

        elif user_choice == 3:
            edit_records(records)

        elif user_choice == 4:
            delete_records(records)

        elif user_choice == 5:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()                        






