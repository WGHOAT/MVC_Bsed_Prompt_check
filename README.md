# **<ins>MVC_Bsed_Prompt_check</ins>**
Check if the Given JSON Input data fits the Prompt Rule If not return Invalid prompt if any fields are missing from the given data return Missing Data

## <ins>**Prompt Rules**</ins> :
     PROMPT_RULES = {
    ("Commercial Auto", "Structure", "Summary Report"): "Prompt 1",
    ("General Liability", "Summarize", "Deposition"): "Prompt 2",
    ("Commercial Auto", "Summarize", "Summons"): "Prompt 3",
    ("Workers Compensation", "Structure", "Medical Records"): "Prompt 4",
    ("Workers Compensation", "Summarize", "Summons"): "Prompt 5",
    }
this is the Rules that Given Output should match 

## <ins>**CASE 1**</ins> :
          - If the Input Data Matches the Rules then Return the Prompt number that matches the data
## <ins>**CASE 2**</ins>: *Error Case*
          - If the Input Data doesnt Follow the Rules then Return Invalid Prompt Error
## <ins>**CASE 3**</ins>: *Error Case*
          - If the Input Data have missing fields then Return Missing Data Error


## <ins>**TechStack to Follow**</ins> :
            - flask
