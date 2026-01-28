import requests
import random
import time

FORM_URL = "" # paste your google form link here with end route /formResponse

# SECTION 4: Likert Scale
likert_options = [
    "Strongly agree",
    "Agree",
    "Neutral",
    "Disagree",
    "Strongly disagree"
]

likert_entry_ids = [
    "entry.964040396",
    "entry.33556787",
    "entry.1274681142",
    "entry.720586861",
    "entry.2077987789",
    "entry.764536819",
    "entry.1916434235",
    "entry.359128807",
    "entry.1939379871",
    "entry.1395567766"
]

# SECTION 5: Describes me scale 
describe_options = [
    "Does not describe me well",
    "Describes me slightly",
    "Describes me moderately",
    "Describes me well",
    "Describes me very well" 
]

describe_entry_ids = [
    "entry.331917349",
    "entry.354033802",
    "entry.1669151633",
    "entry.74772844",
    "entry.2062003336",
    "entry.356332464",
    "entry.1329089558",
    "entry.623180849",
    "entry.997772000",
    "entry.636313511",
    "entry.524077937",
    "entry.823890474",
    "entry.2099935298",
    "entry.1989147867",
    "entry.2006751939",
    "entry.1806437436",
    "entry.1071482108",
    "entry.1650297211",
    "entry.840544488",
    "entry.1925772704",
    "entry.2052567865",
    "entry.426087134",
    "entry.1905865730",
    "entry.142080353",
    "entry.326433726",
    "entry.1427290230",
    "entry.1001766186",
    "entry.1911505534"
]

# Email generation with gender mapping
male_names = [
    "rahul", "aman", "rohan", "arjun", "aditya",
    "raj", "kunal", "vikram", "siddharth", "karan", "nikhil",
    "varun", "harsh", "ravi", "ankit", "akash", "mohit",
    "abhishek", "deepak", "amit", "vishal", "gaurav", "sachin",
    "sandeep", "yash"
]

female_names = [
    "sneha", "pooja", "priya", "kavya",
    "anjali", "neha", "riya", "simran", "divya", "shruti",
    "nisha", "preeti", "ayesha", "tanvi", "isha", "mehak",
    "sakshi", "aditi", "aarti", "swati", "nikita",
    "kritika", "pallavi", "jyoti", "shweta", "samruddhi","nida","ujala",
]

last_names = [
    "sharma", "patel", "verma", "singh", "mehta", "gupta", 
    "kumar", "reddy", "joshi", "nair", "agarwal", "pandey",
    "rao", "iyer", "shah", "malhotra", "kapoor", "chopra"
]

# SECTION 2: Consent options 
consent_options = ["Yes, i agree to participate"] 

# SECTION 3: Demographics 
age_options = ["18-20", "20-22", "23-25"]

# -------- Run automation --------
def submit_form(num_submissions=5):
    """Submit the form multiple times with random data"""
    
    successful = 0
    failed = 0
    
    for i in range(num_submissions):
        # Randomly choose between male and female name
        is_female = random.choice([True, False])
        
        if is_female:
            first_name = random.choice(female_names)
            gender = "Female"
        else:
            first_name = random.choice(male_names)
            gender = "Male"
        
        # Generate email with chosen name
        email = f"{first_name}{random.choice(last_names)}{random.randint(10,99)}@gmail.com"
        
        # Build form data
        data = {
            # SECTION 1: Email
            "entry.1968353436": email,
            
            # SECTION 2: Consent
            "entry.610012877": random.choice(consent_options),
            
            # SECTION 3: Demographics
            "entry.1616223555": random.choice(age_options),
            "entry.939153804": gender,
            
            # Important: Page history to simulate navigating through all sections
            "pageHistory": "0,1,2,3,4,5",
            
            # Optional: Form validation
            "fvv": "1"
        }
        
        # SECTION 4: Fill Likert scale questions
        for eid in likert_entry_ids:
            data[eid] = random.choice(likert_options)
        
        # SECTION 5: Fill "Describes me" questions
        for eid in describe_entry_ids:
            data[eid] = random.choice(describe_options)
        
        # Submit the form
        try:
            r = requests.post(FORM_URL, data=data, allow_redirects=False)
            
            print(f"\n{'='*60}")
            print(f"Submission #{i+1}/{num_submissions}")
            print(f"{'='*60}")
            print(f"Email: {email}")
            print(f"Age: {data['entry.1616223555']}")
            print(f"Gender: {data['entry.939153804']}")
            print(f"Status Code: {r.status_code}")
            
            # Check if successful
            if r.status_code in [200, 302]:
                print("SUCCESS - Form submitted")
                successful += 1
            else:
                print("WARNING - Unexpected status code")
                print(f"Response preview: {r.text[:200]}")
                failed += 1
            
            # Delay between submissions to avoid rate limiting
            if i < num_submissions - 1:
                delay = random.uniform(2, 4)
                print(f"⏳ Waiting {delay:.1f}s before next submission...")
                time.sleep(delay)
                
        except Exception as e:
            print(f"ERROR: {e}")
            failed += 1
    
    # Summary
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total: {num_submissions}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    NUM_SUBMISSIONS = 3                       # type in the num of submissions you wanna do
    
    print("\nStarting Google Form Auto-Filler")
    print(f"Target: {NUM_SUBMISSIONS} submissions")
    print(f"Starting at: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    submit_form(NUM_SUBMISSIONS)
    
    print("Auto-fill completed!")
