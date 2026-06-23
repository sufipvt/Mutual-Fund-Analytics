import pandas as pd 
import os # reading files and folders

folder = "data/raw" 
files = os.listdir(folder) # It looks inside a folder and returns everything inside

print("JOB 1: Load and look at every file")
print()

all_data = {} # create an empty dictionary 

for file_name in files:
    file_path = os.path.join(folder, file_name)
    df = pd.read_csv(file_path)
    all_data[file_name] = df
    print("file:", file_name)
    print("Rows and columns:", df.shape)
    print("First 3 rows:")
    print(df.head(3))
    print("-" * 50)


print(" JOB 2: explore fund master file")

fund_master = all_data['01_fund_master.csv']

print("fund houses in our data")
print(fund_master['fund_house'].unique())
print()

print("fund categories")
print(fund_master['category'].unique())
print()

print("sub categories")
print(fund_master['sub_category'].unique())
print()

print("How many funds total?", len(fund_master))

print("-"*50)

print("JOB 3: Check fund codes match between files ")
print()

nav_history = all_data['02_nav_history.csv']

# Get the list of unique codes in each file
code_in_master = fund_master['amfi_code'].unique()
code_in_nav = nav_history['amfi_code'].unique()

# length of all the funds 
print("no of funds in fund master", len(code_in_master))
print("no of funds in nav history", len(code_in_nav))

missing_codes =[]
for code in code_in_master:
    if code not in code_in_nav:
        missing_codes.append(code)
    
if len(missing_codes) == 0:
     print("All good! Every fund in fund_master has price data in nav_history.")
else:
    print("WARNING: these fund codes have no price data:", missing_codes)
    


