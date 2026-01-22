def record_spell(spel_name: str, ingredients: str)-> str:
    from .validator import validate_ingredients
    validation = validate_ingredients(ingredients)
    if "VALID" in validation:
        return f"Spell recorded: {spel_name} ({validation})"
    return f"Spell rejected: {spel_name} (validation)"
    
