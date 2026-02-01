from openai import OpenAI; import os
client=OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def call_llm(p): return client.chat.completions.create(model='gpt-4',messages=[{'role':'user','content':p}],temperature=0.2).choices[0].message.content
