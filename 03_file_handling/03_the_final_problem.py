# =====================================================================
# THE GRAND FINALE: Full File Operations, CSV, Strings & Error Handling
# =====================================================================
import csv
import os

# Step 1: Setup Raw Log
with open("raw_factory_log.txt", "w") as f: 
    f.write("System: Operational\nCore_Status: Glitched\nError_Count: 999") 

# Step 2: Safe String Patching
with open("raw_factory_log.txt", "r") as f: 
    log_data = f.read() 

new_data = log_data.replace("Glitched", "Optimized") 
new_data = new_data.replace("999", "0") 

with open("patched_factory_log.txt", "w") as f: 
    f.write(new_data) 

# Step 3: Line-by-Line List Extraction
with open("patched_factory_log.txt", "r") as f: 
    list_1 = f.readlines()
    
# Grab the specific lines and clean up the invisible \n tags
status_value = list_1[1].strip()  
error_value = list_1[2].strip()   

# Step 4: Structured CSV Generation 
with open("factory_report.csv", "w", newline='') as f: 
    writer = csv.writer(f) 
    writer.writerow(['Metric', 'Current_Value']) 
    writer.writerow(['Core_Status', status_value])  
    writer.writerow(['Error_Count', error_value])    

# Step 5: Bulletproof Read Verification
try: 
    with open("factory_report.csv", "r") as f: 
        csv_reader = csv.reader(f) 
        for row in csv_reader: 
            print(row, flush=True) 
except FileNotFoundError: 
    print("Report file is missing! Please check the system.") 
finally: 
    print("--- Final System Verification Audit Complete ---") 

# Step 6: Disk Cleanup
os.remove("raw_factory_log.txt") 
os.remove("patched_factory_log.txt")
