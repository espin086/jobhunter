import os
import re

def menu():
    while True:
        print("╔══════════════════════════════╗")
        print("║         Job Hunter           ║")
        print("║     Find Your Dream Job      ║")
        print("╠══════════════════════════════╣")
        print("║    1. Upload Resume          ║")
        print("║    2. Search Jobs            ║")
        print("║    3. View Saved Jobs        ║")
        print("║    q. Quit                   ║")
        print("╚══════════════════════════════╝")

        choice = input("Enter your choice: ")


        if choice == '1':
            # Do upload resume
            file_path = input("Enter the path to your resume file: ")
            if os.path.exists(file_path):
                os.system(f"python3 ../jobhunter/utils/file_converter.py {file_path}")
                os.system(f"python3 ../jobhunter/utils/job_title_generator.py --resume_file /Users/jjespinoza/Documents/jobhunter/jobhunter/resumes/resume.txt ")
            else:
                print("Invalid file path. Please try again.")
            pass

        elif choice == '2':
            # Do search jobs
            search_term = str(input("Enter job title: "))
            search_term = re.sub(r'[^\w\s]', '_', search_term)
            search_term = re.sub(r'\s', '_', search_term)
            
            location = str(input("Enter location or remote: "))
            location = re.sub(r'[^\w\s]', '_', location)
            location = re.sub(r'\s', '_', location)

            os.system(f"python3 ../jobhunter/linkedin_bot.py {search_term} {location} 0 0 ")
            os.system(f"python3 ../jobhunter/utils/database.py")
            os.system(f"python3 ../jobhunter/utils/clean_data_loader.py")
            pass
        
        elif choice == '3':
            # Do view saved jobs
            os.system(f"python3 ../jobhunter/utils/get_latest_jobs.py")
            pass
        elif choice == 'q':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

menu()