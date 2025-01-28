from box import Box

lvals = [str(i) for i in range(1, 21)]
bvals = [str(i) for i in range(1, 21)]







cpl = Box({
    "Fighter": ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],
    "Rogue": ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Sleight of Hand", "Stealth"],
    "Wizard": ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"],
    "Cleric": ["History", "Insight", "Medicine", "Persuasion", "Religion"]
})
