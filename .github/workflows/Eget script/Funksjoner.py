import pandas as pd
from pathlib import Path

def hent_aktuell_spillerdata(base_path):
    base = Path(base_path)
    
    # 1. Finn siste ferdige gameweek
    gw_summaries = pd.read_csv(base / "gameweek_summaries.csv")
    ferdige = gw_summaries[gw_summaries["finished"] == True]
    siste_gw_id = int(ferdige["id"].max())
    
    # 2. Les playerstats fra riktig GW-mappe
    gw_mappe = base / "By Gameweek" / f"GW{siste_gw_id}"
    df = pd.read_csv(gw_mappe / "playerstats.csv")
    
    return df, siste_gw_id

BASE_PATH = r"/Users/casperolsen/Documents/GitHub/FPL-Elo-Insights/data/2025-2026"
df, siste_gw = hent_aktuell_spillerdata(BASE_PATH)

def høyest_ppg(df):
    _, ppg = next(df.iterrows())
    ppg = df.iloc[0]
    for _, spiller in df.iterrows():
        if float(spiller['points_per_game']) > float(ppg['points_per_game']):
            ppg = spiller
    return ppg

ppg = høyest_ppg(df)
print(ppg["first_name"], ppg["points_per_game"])
