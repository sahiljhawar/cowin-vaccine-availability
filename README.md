# Python CLI Script to check CoWIN vaccination slot

This script can be used to check the availability of vaccination slots using CoWIN API.
The program is inspired from [cowin-vaccination-slot-availability](https://github.com/bhattbhavesh91/cowin-vaccination-slot-availability) and [PyCowinAPI](https://github.com/Kunal-Kumar-Sahoo/PyCowinAPI).

## Usage

- Clone the repository on your system.
- Install the dependencies using `pip3 install -r requirements.txt`
- Open CMD in root folder and run the Python script `python main.py`
- Open `csvjson.py` in text editor and check for your near about `district_id`.

## Current situation

- Right now, details can only be found using `district_id`.
- User can search using multiple `district_id`, invalid `district_id` will be shown to the user and will be ignored.
- Minor bugs/code formatting issues will be there.

<! --- ## Future changes --->

- More functionality will be added to the script.
- Query using `state_id` and `pincode` will be added.
- Will document everything in future commits.
- Planning to clone the same project and modify it to run it on cloud and send notifications via IFTTT (_uncertain as of now_). 

## Demo

```
D:\Python\vaccination>python main.py
For which day you want to enquire for?
    0: Today
    1: Tomorrow
    2: Day after tomorrow and so forth

>>> 0

Choose your vaccine:
    1: COVAXIN
    2: COVISHIELD

>>> 1

Enter district codes (enter comma separated values): 505,506

[] is/are invalid code/s


Vaccine availability at ['Jaipur I', 'Jaipur II']
+-------------------------------------------------------------------------------------------------------------+
|                                             Availabilty Details                                             |
+------------+---------+-----------------+--------------------------------+-------------+---------+-----------+
|    DATE    | PINCODE |    BLOCK NAME   |              NAME              | AVAILABLITY | VACCINE | AGE LIMIT |
+------------+---------+-----------------+--------------------------------+-------------+---------+-----------+
| 12-05-2021 |  302005 |  Jaipur I Urban | Covaxin VidhanSabha Only Staff |      0      | COVAXIN |     45    |
| 12-05-2021 |  302017 | Jaipur II Urban |        UPHC Ward No. 46        |      0      | COVAXIN |     45    |
| 13-05-2021 |  302017 | Jaipur II Urban |     Fortis Hospital CVC 1      |      0      | COVAXIN |     18    |
| 13-05-2021 |  302018 | Jaipur II Urban |        Raghu Vihar Cvc         |      0      | COVAXIN |     45    |
| 13-05-2021 |  302020 |     Sanganer    |       Triveni Nagar Cvc        |      0      | COVAXIN |     45    |
| 12-05-2021 |  303007 |     Chakshu     |       Padampura Covaxin        |      0      | COVAXIN |     45    |
| 13-05-2021 |  303102 |   Virat Nagar   |    Covaxin BCMO VIRATNAGAR     |      0      | COVAXIN |     45    |
| 13-05-2021 |  303103 |     SHAHPURA    |      BCMO Office Shahpura      |      0      | COVAXIN |     45    |
| 12-05-2021 |  303104 |     SHAHPURA    | Ayurvedic Hospital MANOHARPUR  |      0      | COVAXIN |     45    |
| 12-05-2021 |  303301 |      Bassi      |          Tunga Covxin          |      0      | COVAXIN |     45    |
| 13-05-2021 |  303338 |     Sambhar     |    Phulera Railway Covexine    |      0      | COVAXIN |     45    |
| 12-05-2021 |  303903 |     Chakshu     |        KADERA Covaxine         |      0      | COVAXIN |     45    |
| 12-05-2021 |  303903 |     Chakshu     |        Titriya Covaxin         |      0      | COVAXIN |     45    |
| 12-05-2021 |  342601 |      Bassi      |      Sambhariya Covexine       |      0      | COVAXIN |     45    |
+------------+---------+-----------------+--------------------------------+-------------+---------+-----------+
```

# Issues 

For some reason [findByDistrict](https://apisetu.gov.in/public/marketplace/api/cowin#/Appointment%20Availability%20APIs/findByDistrict) is not working for certain districts and dates

---

# Contributions

Feel free to add to the current project. Further API call methods can be found on [API Setu](https://apisetu.gov.in/public/marketplace/api/cowin).

---

# Social

<a href="https://www.linkedin.com/in/sahil-jhawar/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>
<a href="https://instagram.com/jhawarji" target="_blank"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"></a>
<a href="https://github.com/sahiljhwar" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>
