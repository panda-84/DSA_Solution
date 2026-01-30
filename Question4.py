def smart_energy_grid():
    demand = {
        6: {"A": 20, "B": 15, "C": 25},
        7: {"A": 22, "B": 16, "C": 28}
    }
    sources = [
        {"type": "Solar", "capacity": 50, "start": 6, "end": 18, "cost": 1.0},
        {"type": "Hydro", "capacity": 40, "start": 0, "end": 24, "cost": 1.5},
        {"type": "Diesel", "capacity": 60, "start": 17, "end": 23, "cost": 3.0}
    ]
    total_cost = 0
    diesel_hours = []
    for hour, districts in demand.items():
        total_demand = sum(districts.values())
        min_limit = total_demand * 0.9

        available = [s.copy() for s in sources if s["start"] <= hour <= s["end"]]
        available.sort(key=lambda x: x["cost"])

        remaining = total_demand
        allocation = {}

        for src in available:
            if remaining <= 0:
                break
            used = min(src["capacity"], remaining)
            allocation[src["type"]] = used
            remaining -= used
            total_cost += used * src["cost"]
            if src["type"] == "Diesel" and used > 0:
                diesel_hours.append(hour)
        print(f"\nHour {hour}")
        print("Allocation:", allocation)
        print("Demand Fulfilled:", total_demand - remaining, "kWh")
    print("\nTotal Cost (Rs.):", total_cost)
    print("Diesel Used At Hours:", diesel_hours)
smart_energy_grid()
