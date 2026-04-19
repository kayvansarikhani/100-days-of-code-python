# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# city = ["Paris", "Lille", "Dijon"]
# print(city[1])

# print(travel_log["France"][1])
#
# nested_list = ["A", "B", ["C", "D"]]
#
# print(nested_list[2][0])
# print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visisted": ["Paris", "Lille", "Dijon"],
        "total_visits": 8,
    },
    "Germany": {
        "cities_visited": ["Stuttgart", "Berlin"],
        "total_visits": 5
    },
}

print(travel_log["Germany"]["cities_visited"][0],
      travel_log["Germany"]["total_visits"])
