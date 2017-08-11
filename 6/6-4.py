glossary = {"variable": "Holds a value, or information associated with the variable.",
            "string": "A series of characters within quotes.",
            "whitespace": "Any nonprinting character", "float": "Any number with a decimal point.",
            "comment": "Comments within programs that do not affect the program itself."}

for term, defi in glossary.items():
    print(term.title() + ": " + defi)