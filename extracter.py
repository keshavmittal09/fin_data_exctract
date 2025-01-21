import openai 
# from openai_apikey import apik
# from dotenv import load_dotenv
import os

def api_out(prompt):
    openai.api_key=os.getenv("apik")

    response = openai.chat.completions.create(
        model="gpt-4o-mini",    
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    cont = response.choices[0].message.content
   
    return cont

def def_prompt(data):
    prompt ="""Can you analyze the given data and return the company name,owned by, revenue, net profit, and EPS in the following dictionary format?,you may use other resources to collect data or browse internet , or the data you know (i.e :- name of the owner ect.)
    If the information is not available, leave the fields blank (i.e., ""). 
    Do not include anything else in the response. Only return the JSON data.

    Output format (in JSON): 
    {
        "company_name": "",
        "owned by": "",
        "revenue": "",
        "net_profit": "",
        "EPS": ""
    }

    The data is: 
    """
    prompt += data 

    d = api_out(prompt)
    return d






