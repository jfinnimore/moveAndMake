# script to combine files

from pathlib import Path
import pandas as pd

this_dir = Path(__file__).resolve().parent

parts = []
for path in (this_dir / "PROC_REASON*.csv*"):
  print(f'Reading {path.name}')
  part = pd.read_csv(path, index_col="CASE_NUMBER")
  parts.append(part)
  
 df=pd.concat(parts)

pivot=pd.pivot_table(df,
                     index="CASE_NUMBER", columns="PROCEDURE",
                     index="SURGERY_MINUTES", aggfunc="sum")

summary = pivot.resample("M").sum()
summary.index.name = "Month"

summary.to_excel(this_dir / "reason_report_pandas.xlsx")
