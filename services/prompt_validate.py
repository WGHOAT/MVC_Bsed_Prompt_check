

#Prompt Rules
PROMPT_RULES = {
    ("Commercial Auto", "Structure", "Summary Report"): "Prompt 1",
    ("General Liability", "Summarize", "Deposition"): "Prompt 2",
    ("Commercial Auto", "Summarize", "Summons"): "Prompt 3",
    ("Workers Compensation", "Structure", "Medical Records"): "Prompt 4",
    ("Workers Compensation", "Summarize", "Summons"): "Prompt 5",
    }

# i f the given input is empty or missing any one of the must_fields the raise value error
def prompt_validation(query) :
    must_fields = {'situation','level','field_type','data'}
    if not query :
        raise ValueError("Missing Fields")
    if not must_fields.issubset(query.keys()):
        raise ValueError("Missing Fields")

def prompt_check(query) :
    key = (query['situation'],query['level'],query['field_type'])
    if key in PROMPT_RULES:
        return PROMPT_RULES[key]
    else:
        raise ValueError("Missing Data")


