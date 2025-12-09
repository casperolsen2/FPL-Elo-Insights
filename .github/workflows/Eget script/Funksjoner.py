import pandas as pd
from pathlib import Path
from Lese_Nyeste_GW import siste_stats_per_spiller


ps = pd.read_csv("data/2025-2026/playerstats.csv")
ps_clean = siste_stats_per_spiller(ps)

def høyest_ppg(ps_clean):
    _, ppg = next(ps_clean.iterrows())
    ppg = ps_clean.iloc[0]
    for _, spiller in ps_clean.iterrows():
        if float(spiller['points_per_game']) > float(ppg['points_per_game']):
            ppg = spiller
    return ppg

def dyreste_spiller(ps_clean):
    _, dyreste = next(ps_clean.iterrows())
    dyreste = ps_clean.iloc[0]
    for _, spiller in ps_clean.iterrows():
        if spiller['now_cost'] > dyreste['now_cost']:
            dyreste = spiller
    return dyreste

def moneyball(ps_clean):
    _, moneyball = next(ps_clean.iterrows())
    moneyball = ps_clean.iloc[0]
    for _, spiller in ps_clean.iterrows():
        if spiller['total_points'] == 0:
            continue
        if spiller['total_points'] / spiller['now_cost'] > moneyball['total_points'] / moneyball['now_cost']:
            moneyball = spiller
    return moneyball

#print(moneyball(ps_clean)['second_name'], moneyball(ps_clean)['first_name'])

def moneyball_topp_10(ps_clean):
    liste = ps_clean[(ps_clean['total_points'] > 0) & (ps_clean["now_cost"] > 0)].copy()
    liste['value'] = liste['total_points'] / liste['now_cost']

    topp10 = liste.sort_values("value", ascending = False).head(10)
    return topp10

def best_form_topp_10(ps_clean):
    liste = ps_clean[(ps_clean['form']>0)]
    
    topp10 = liste.sort_values("form", ascending = False).head(10)
    return topp10

def print_spiller(ps_clean, spiller):
    temp = None
    for _, sp in ps_clean.iterrows():
        if spiller.lower() == str(sp['second_name']).lower():
            temp = sp
    return f"{temp['first_name']}, {temp['second_name']} - {temp['form']} form - {temp['now_cost']} pris"

#print(best_form_topp_10(ps_clean)['web_name'])
#print(print_spiller(ps_clean, "m.salah"))