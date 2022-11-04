from teambrobro import app
from flask import request
import requests

url = "https://free-nba.p.rapidapi.com/teams"

headers = {
    "X-RapidAPI-Key": "9275b62a1fmsh3b832340dafb492p1abc77jsn58ef554feee6",
    "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

response.raise_for_status()
if response.status_code != 204:
    teams_json = response.json()['data']

teams_list = []

logos = [
    'https://user-images.githubusercontent.com/111609656/199171378-41fa35f7-2b0c-40d6-bb10-1509fd534520.png',
    'https://user-images.githubusercontent.com/111609656/199171381-223f1714-2c27-4fad-9d10-0fb492396c19.png',
    'https://user-images.githubusercontent.com/111609656/199171384-eb285549-9dc6-4bc0-92fb-9398936ac29b.png',
    'https://user-images.githubusercontent.com/111609656/199171386-88d39e7f-317f-4e99-a943-7ed7ac2cfcce.png',
    'https://user-images.githubusercontent.com/111609656/199171394-bb4ef3f9-816d-42e3-b7f2-6b71a519394c.png',
    'https://user-images.githubusercontent.com/111609656/199171402-7682db65-2dfb-4b25-883d-a287bcce7c9b.png',
    'https://user-images.githubusercontent.com/111609656/199171404-e6441c68-5f28-49d3-bbe8-f909a9a02013.png',
    'https://user-images.githubusercontent.com/111609656/199171410-41834357-f37e-4691-b2ff-f444c7256adc.png',
    'https://user-images.githubusercontent.com/111609656/199171420-d6a48c42-3f64-4331-855c-940cfeed7d60.png',
    'https://user-images.githubusercontent.com/111609656/199171427-f22d179d-181f-4194-bdad-878739527806.png',
    'https://user-images.githubusercontent.com/111609656/199171431-951409b4-3fa5-47ad-8c87-c3d0dbb84ae4.png',
    'https://user-images.githubusercontent.com/111609656/199171437-67c5ffde-f292-4891-a149-0e1aa183889f.png',
    'https://user-images.githubusercontent.com/111609656/199171443-a1973415-d629-458b-b189-4aa1be923595.png',
    'https://user-images.githubusercontent.com/111609656/199171453-b052e1a0-25b9-4832-afe5-dba3eda409a6.png',
    'https://user-images.githubusercontent.com/111609656/199171468-c7bbed10-b2ac-48bc-8bc4-aa89ba8ea050.png',
    'https://user-images.githubusercontent.com/111609656/199171474-72895807-1c63-44fb-b80e-a0c1885f0d4e.png',
    'https://user-images.githubusercontent.com/111609656/199171483-28b1bc31-5a9e-4b20-9dfe-c00def963562.png',
    'https://user-images.githubusercontent.com/111609656/199171492-fe77c41e-f4c8-4d46-a8d0-cf7324b0dead.png',
    'https://user-images.githubusercontent.com/111609656/199171501-2e8c43f6-ea8d-42c8-8414-bddaf5ba964c.png',
    'https://user-images.githubusercontent.com/111609656/199171512-8f15c332-282f-49f9-97bf-1266c9c904f3.png',
    'https://user-images.githubusercontent.com/111609656/199171513-ecdd8453-2fcb-4bae-aab0-2a07f161e393.png',
    'https://user-images.githubusercontent.com/111609656/199171522-be41953d-f4a4-40ef-93a2-ac27d8be9f7d.png',
    'https://user-images.githubusercontent.com/111609656/199171535-7231e284-c5e8-43ca-a7a4-78cec2c67bfc.png',
    'https://user-images.githubusercontent.com/111609656/199171543-6d3809e7-682b-4a32-956b-7eafc21fe85c.png',
    'https://user-images.githubusercontent.com/111609656/199171551-70bcf2d9-b6ba-4cdb-99f5-01f5b0e76d3f.png',
    'https://user-images.githubusercontent.com/111609656/199171556-a17cc81f-8815-4803-b634-d83467d9ba76.png',
    'https://user-images.githubusercontent.com/111609656/199171561-9ec46967-4005-44f9-ac79-16aadf574eec.png',
    'https://user-images.githubusercontent.com/111609656/199171568-c2c82b48-f456-4d4f-966e-6e98d35702ab.png',
    'https://user-images.githubusercontent.com/69406769/199173873-a56014ec-06f7-43b0-b21b-87241c4b746b.png',
    'https://user-images.githubusercontent.com/69406769/199173920-22fb13df-0a8d-4b5a-accd-f0822de301ae.png',
]

for i, item in enumerate(teams_json):
    teams_list.append({"likes": 0, "dislikes": 0, "name": item['full_name'].split()[-1],
                       "abbreviation": item['abbreviation'], "division": item["division"], "city": item['city'], "logo": logos[i]})


@app.route('/')
def index():
    return "PULLUH ONNA GANG TEAM BRO BRO WE AIN NEVA PLAYIN U DON WANT NO SMOKE WIT NO TEAM BRO BRO SLATT SLATT WE DA PGK PGK"


@app.route('/like', methods=["POST"])
def like():
    data = request.json
    id = data["id"]
    teams_list[id]["likes"] += 1
    return {"likes": teams_list[id]["likes"]}


@app.route('/dislike', methods=["POST"])
def dislike():
    data = request.json
    id = data["id"]
    teams_list[id]["dislikes"] += 1
    return {"dislikes": teams_list[id]["dislikes"]}


@app.route('/teams', methods=["GET"])
def teams():
    return teams_list