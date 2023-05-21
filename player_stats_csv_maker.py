from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType

import pandas as pd
import time
import json

final_json = []
# Grab player ids from text file line by line and run through library 1 by 1, outputting to csv
with open('player_ids.txt') as file:
    for line in file:
        # Call the library
        json_stats = json.loads(client.regular_season_player_box_scores(player_identifier=line.strip(), season_end_year=2023, output_type=OutputType.JSON))
        for x in json_stats:
            x.update({"player_id":line.strip()})
            final_json.append(x)

        # Wait 3 seconds to avoid getting rate limited
        time.sleep(3)

# Export from json to csv
json_obj = json.dumps(final_json)
df = pd.read_json(json_obj)
df.to_csv('test.csv')