import openai

# Set your API key
openai.api_key = 'your-api-key-here'

# Make a request to the API
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or a different model you want to use
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

# Print the response
print(response.choices[0].message['content'])
