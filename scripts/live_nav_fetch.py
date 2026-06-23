import requests 
import pandas as pd
import os 

# Fetch live NAV data from MFAPI and save it as raw CSV.

os.makedirs("data/raw", exist_ok=True) # create a folder if doenst exist and if exists then no issue 

funds = {
    "hdfc_top100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for fund_name, code in funds.items():
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data['data'])
    df["scheme_name"] = data["meta"]["scheme_name"]
    df["scheme_code"] = data["meta"]["scheme_code"]
    
    output_file = os.path.join("data", "raw", f"{fund_name}.csv")

    df.to_csv(output_file, index = False)

    print(f"saved: {output_file}")
