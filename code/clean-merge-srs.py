import os
import pandas as pd

years = (1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2021,2022)

df = pd.DataFrame()
for year in years:
    df_year = (pd.read_csv(os.path.join("data", "raw", "srs", f"{year}-ratings-sports-reference.csv")))
    df_year["year"] = year
    df = pd.concat([df, df_year])

df.to_csv(os.path.join("data", "clean", "team-ratings.csv"), index = False)