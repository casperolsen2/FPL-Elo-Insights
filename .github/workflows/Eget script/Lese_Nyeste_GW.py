import pandas as pd
import pathlib as path

ps = pd.read_csv("data/2025-2026/playerstats.csv")

def siste_stats_per_spiller(ps: pd.DataFrame) -> pd.DataFrame:
    ps = ps.copy()
    ps["total_points"] = pd.to_numeric(ps["total_points"], errors="coerce")

    # finn index til raden med høyest total_points for hver spiller-id
    idx = ps.groupby("id")["total_points"].idxmax()

    # velg bare disse radene
    clean = ps.loc[idx].reset_index(drop=True)
    return clean

ps_clean = siste_stats_per_spiller(ps)