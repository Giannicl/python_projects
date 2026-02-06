from typing import List, Dict 

def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    sorted_list = sorted(artifacts, key=lambda item: item["power"], reverse=True)
    return sorted_list

def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    filtered_mages = list(filter(lambda item: item["power"] >= min_power, mages))
    return filtered_mages

def spell_transformer(spells: List[str]) -> List[str]:
    mapped_spells = list(map(lambda item: f"* {item} *", spells))
    return mapped_spells

def mage_stats(mages: List[Dict]) -> Dict:
    max_power = max(mages, key=lambda item: item['power'])['power']
    min_power = min(mages, key=lambda item: item['power'])['power']
    total_power = sum(map(lambda item: item['power'],mages))
    avg_power = round(total_power / len(mages), 2)
    stats = { 
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power,
    }
    return stats

def main()-> None:
    print("Testing artifact sorter...")
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'magic'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power) comes before {sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)")
    
    print("\nTesting spell transformer...")
    spells = ['fireball', 'heal', 'shield']
    transformed = spell_transformer(spells)
    print(f" {transformed[0]} {transformed[1]} {transformed[2]}")

main()
