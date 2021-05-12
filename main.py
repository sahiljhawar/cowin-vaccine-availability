from csvjson import district_codes as dc
from prettytable import PrettyTable
import requests
import datetime
import json

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'
}
gen_det = ["name", "block_name", "pincode", "sessions"]
vac_det = ["available_capacity", "vaccine", "date", "min_age_limit"]


def get_key(val: str) -> str:
    for key, value in dc.items():
        if val == value:
            return key

    return "Invalid key value"


def get_vaccine_details(n: str, x: int) -> None:
    n = n.upper()

    dst_code = {x for x in input("Enter district codes (enter comma separated values): ").split(',')}
    print()

    a = {code for code in dst_code if code not in dc.values()}

    codes = dst_code ^ a  #extracting correct input district codes from invalid input and all input codes

    print([i for i in a if a not in dc.values()], "is/are invalid code/s\n\n")

    print("Vaccine availability at", [get_key(i) for i in codes])
    
    t = PrettyTable([
        "DATE", "PINCODE", "BLOCK NAME", "NAME", "AVAILABLITY", "VACCINE",
        "AGE LIMIT"
    ],
                    title="Availabilty Details",
                    sortby="PINCODE")
    for code in codes:
        URL = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={code}&date={date(x)}"
        response = requests.get(URL, headers=headers)
        if (response.ok) and ('centers' in json.loads(response.text)):
            resp_json = response.json()
            json_object = json.dumps(resp_json, indent=4)
            for i in resp_json.get("centers"):
                if (i.get(gen_det[3])[0]).get(vac_det[1]) == n:
                    t.add_row([(i.get(gen_det[3])[0]).get(vac_det[2]),
                               str(i.get(gen_det[2])),
                               str(i.get(gen_det[1])),
                               str(i.get(gen_det[0])),
                               str((i.get(gen_det[3])[0]).get(vac_det[0])),
                               (i.get(gen_det[3])[0]).get(vac_det[1]),
                               (i.get(gen_det[3])[0]).get(vac_det[3])])
    print(t)


print("For which day you want to enquire for?\n\
    0: Today\n\
    1: Tomorrow\n\
    2: Day after tomorrow and so forth\n")
day = int(input(">>> "))
print()

print("Choose your vaccine:\n\
    1: COVAXIN\n\
    2: COVISHIELD\n")
choice = input(">>> ")
print()

date = lambda x: (datetime.datetime.today() + datetime.timedelta(x)).strftime("%d-%m-%Y")

if choice == "1":
    get_vaccine_details("COVAXIN", day)
elif choice == "2":
    get_vaccine_details("COVISHIELD", day)
else:
    print("Not a valid option")