import json
import re

# regex = r"Product: .*\n"
# regex = r"Manufacturer: .*\n"
regex = r"SerialNumber: .*\n"

# json_list = "prod"
# json_list = "manufact"
json_list = "serial"

def load_data(filePath):

    with open(filePath) as file:
        data = file.read()

    return data

def clean(input_data):
    cleaned = []
    for s in input_data:
        p = s.split(":")

        if len(p) == 2:
            p_id = p[1].strip()
            cleaned.append(p_id) 
    return cleaned

def grab_section(regex):
    return clean(re.findall(regex, syslog))

# Grabs all ID values from the script
syslog = load_data("./syslog")
section = grab_section(regex)

auth_json = json.loads(load_data("./auth.json"))
auth_json_dict = { i : "" for i in auth_json[json_list] }

count = 0
for i, x in enumerate(section):

    if not x in auth_json_dict:
        count += 1
        print(x)
