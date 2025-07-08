# MVC_Bsed_Prompt_check
Check if the Given JSON Input data fits the Prompt Rule If not return Invalid prompt if any fields are missing from the given data return Missing Data

# Prompt Rules :
     PROMPT_RULES = {
    ("Commercial Auto", "Structure", "Summary Report"): "Prompt 1",
    ("General Liability", "Summarize", "Deposition"): "Prompt 2",
    ("Commercial Auto", "Summarize", "Summons"): "Prompt 3",
    ("Workers Compensation", "Structure", "Medical Records"): "Prompt 4",
    ("Workers Compensation", "Summarize", "Summons"): "Prompt 5",
}
this is the Rules that Given Output should match 

## CASE 1 :
          - If the Input Data Matches the Rules then Return the Prompt number that matches the data
## CASE 2 : Error Case
          - If the Input Data doesnt Follow the Rules then Return Invalid Prompt Error
## CASE 3 : Error Case
          - If the Input Data have missing fields then Return Missing Data Error
