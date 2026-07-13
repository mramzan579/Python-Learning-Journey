# CHALLENGE 1: Basic File Handling (r+ Overwrite & a+ Append)
f=open('robo.txt','r+')
data='Robo is Online\nBattery 100%'
f.write(data)
f.seek(0)
print(f.read())
f.close()
f=open('robo.txt','a+')
f.write("\nStatus: Exploring")
f.seek(0)
print(f.read())
f.close()

# CHALLENGE 2: Targeted Overwrite (Using f.seek to change Passcode)
with open('robots.txt','w') as f:
    f.write('hi')
with open('robots.txt','r+') as f:
    DATA='Passcode: 1234\nStatus: Secure'
    f.write(DATA)
    f.seek(10)
    f.write('7989')
    f.seek(0)
    print(f.read())

# CHALLENGE 3: Robot Maintenance Log (r+, a+, and seek index math)
with open('robots.txt','w') as f:
    f.write('System: Active\nErrors: 5   ')
with open('robots.txt','a+') as f:
    f.write('\nLocation: Lab')
    f.seek(0)
    print(f.read())
with open('robots.txt','r+') as f:
    f.seek(24)
    f.write('0')
    f.seek(0)
    print(f.read())

# CHALLENGE 4: The Core Override (Multi-Seek & String Matching)
with open('robots.txt','w') as f:
        f.write("Mode: Offline\nCore: Bad")
with open('robots.txt','r+') as f:
     f.seek(6)
     f.write('Online ')
     f.seek(0)
     f.seek(21)
     f.write('OK ')
with open('robots.txt','a+') as f:
     f.write("\nFix: Success")
     f.seek(0)
     print(f.read())
     
# CHALLENGE 5: Using String .replace() and .find() on Files
with open("robots.txt","w") as f:
    f.write("Danger: Robot is broken. Battery is low.")
with open("robots.txt","r") as f:
     log_data=f.read()
     if ("broken") in log_data:
         print("ALERT: Robot is broken. Please check the system.")
     else:
        print("Robot is functioning properly.")
new=log_data.replace("broken","fixed")
new=new.replace("low","high")
with open("robots.txt","w") as f:
     f.write(new)
with open("robots.txt","r") as f:
     print("Updated Log Data:")
     print(f.read())


# CHALLENGE 6: The AI System Patch (String Chaining Re-match)
with open("ai_confige.txt","w") as f:
     f.write("System Status: Error_404. Model: Old_AI. Version: Beta.")
with open("ai_confige.txt","r") as f:
     config_data=f.read()
     if ("Error_404") in config_data:
          print("Patch Required!")
     else:
          print("System Safe.")
new_data=config_data.replace("Old_AI","New_AI")
new_data=new_data.replace("Beta","Production")
with open("ai_confige.txt","w") as f:
     f.write(new_data)
with open("ai_confige.txt","r") as f:
     print(f.read())