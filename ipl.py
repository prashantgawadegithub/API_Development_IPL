import pandas as pd
import numpy as np

matches=pd.read_csv("ipl-matches.csv")

print(matches.head())

def teamsAPI():
    teams= list(set(list(matches['Team1'])+list(matches['Team2'])))
    team_dict={
        'teams':teams
    }
    return team_dict