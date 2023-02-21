import numpy as np
import pandas as pd
from requests import get
import sys
import json

#Set argument variable as profile ID
profile_id = sys.argv[1]
print(profile_id)

r = get(f"http://steamcommunity.com/profiles/{profile_id}/inventory/json/753/1")
print(r)
print(r.json())
