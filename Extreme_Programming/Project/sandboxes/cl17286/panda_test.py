import csv
import pandas as pd
import os
import re
pd.set_option('display.max_columns', None)
data = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/AccountPassword.csv"))
example = "(Description:google password)"
# (Category:Email)
# re.
regex_rule = re.compile(r'\((Category|Description):(.*?)\)')
new_example_AND = re.sub('\)AND\(',')&(', example)
new_example_OR = re.sub('\)OR\(',')|(', new_example_AND)
search = re.sub(r'\((Category|Description|Username|Password|Name):(.*?)\)',"\\1.str.contains(\"(\\2)\",regex=True,case=False)", new_example_OR)
Final = re.sub(r'\b(.*?)\s+\b(.*?)',r'\1|\2', search)
# final_search = 'Category.str.contains("(Email)", regex=True)&Description.str.contains("(google)", regex=True)'
filter_string = (data['Category'] == 'Email')
print(search)
print(Final)
# result = data.query('Description.str.contains("(google|got)",regex=True)', engine='python')
result = data.query('( UserID == "1")&(Category.str.contains("(Entertainment)",regex=True,case=False))', engine='python' )


                  # 'Category.str.contains("(Email)", regex=True)&Description.str.contains("(abcd)", regex=True)'
data_list = data.values.tolist()
# print(data_list)
# print(data)
result_list = result.values.tolist()
for line in result_list:
    print(line)
# (.*?)(AND)(.*?)
# \1\&\3
# \((Category|Description):(.*?)\)
