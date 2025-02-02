# import source code
from viewing_party.party import *

# import test data
from tests.test_constants import *

# import "pretty-print" library
import pprint
pp = pprint.PrettyPrinter(indent=4)

# play testing section
# print("\n-----Wave 01 test data-----")
# pp.pprint(HORROR_1)
# pp.pprint(FANTASY_1)
# pp.pprint(FANTASY_2)
# movie_to_watch = HORROR_1
# janes_data = {
#         "watchlist": [
#             FANTASY_1,
#             movie_to_watch
#         ],
#         "watched": [FANTASY_2]
#     }
# print(janes_data["watchlist"][0]['title'])

#     # Act
# updated_data = watch_movie(janes_data, movie_to_watch["title"])
# print(updated_data)



# print("\n-----Wave 02 user_data-----")
# pp.pprint(clean_wave_2_data())

#print("\n-----Wave 03 user_data-----")
#pp.pprint(clean_wave_3_data())
amandas_data = clean_wave_3_data()
amandas_data["friends"][0]["watched"].append(INTRIGUE_3)
pp.pprint(amandas_data)

# Wave 04 user data
# print("\n-----Wave 04 user_data-----")
# pp.pprint(clean_wave_4_data())

# Wave 05 user data
# print("\n-----Wave 05 user_data-----")
# pp.pprint(clean_wave_5_data())
