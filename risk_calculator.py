risk_data = {
    "yaounde":   45,
    "douala":    52,
    "bafoussam": 28,
    "bertoua":   18,
    "garoua":    39,
    "limbe":     22,
}

#  Collect 5 cities from the user into a list

user_cities = []  

for i in range(5):
    city = input(f"Enter city #{i + 1}: ").strip().lower()
    user_cities.append(city)

# Loop through the list and check each city

print("\n--- Risk Report ---")

results = {}          
high_risk_count = 0   

for city in user_cities:
    if city not in risk_data:
        print(f"{city.title()}: Unknown city")
        results[city] = "UNKNOWN"
    else:
        score = risk_data[city]

        if score > 40:
            status = "HIGH RISK"
            high_risk_count += 1
        else:
            status = "SAFE"

        print(f"{city.title()}: {status} ({score}/100)")
        results[city] = status

        
print("\n--- Summary ---")
print(f"Cities checked : {len(user_cities)}")
print(f"High risk count: {high_risk_count}")
print(f"Full results   : {results}")
