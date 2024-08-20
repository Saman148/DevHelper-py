from openai import OpenAI
client = OpenAI(api_key='asst_njZ9AwFYwOp49gCuheoUFgY6')

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is a LLM?"}
    ]
)
