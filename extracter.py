import openai 
from openai_apikey import apik







def api_out(prompt):
    openai.api_key=apik

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




# data = """The company was incorporated as Tesla Motors, Inc. on July 1, 2003, by Martin Eberhard and Marc Tarpenning.[10][11] They served as chief executive officer and chief financial officer, respectively.[12] Eberhard said that he wanted to build "a car manufacturer that is also a technology company", with its core technologies as "the battery, the computer software, and the proprietary motor".[13]

# Ian Wright was Tesla's third employee, joined a few months later.[10] In February 2004, the company raised US$7.5 million (equivalent to $12 million in 2023) in series A funding, including $6.5 million (equivalent to $10 million in 2023) from Elon Musk, who had received $100 million from the sale of his interest in PayPal two years earlier. Musk became the chairman of the board of directors and the largest shareholder of Tesla.[14][15][12] J. B. Straubel joined Tesla in May 2004 as chief technical officer.[16]

# A lawsuit settlement agreed to by Eberhard and Tesla in September 2009 allows all five – Eberhard, Tarpenning, Wright, Musk, and Straubel – to call themselves co-founders.[17] it has made over $5 billion in year 2020-21
# """
# data = st.text_area("enter",height=300)

# if st.button("submit"):

#     try:
#         result = json.loads(a)
#         df = pd.DataFrame(result.items(),columns=["Measures","Values"])  # This will print the parsed dictionary if the response is valid JSON
#     except json.JSONDecodeError as e:
#        er = "some error, TRY AGAIN" 
#        pass

# print(type(a)) 


