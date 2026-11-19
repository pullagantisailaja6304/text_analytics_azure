# 4. Use AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-12-01-preview"  # Use a recent stable API version
)

# 5. Call the model (model parameter uses deployment name)
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "you are an AI assistent extract only key phrases from user content"},
        {"role": "user", "content": "location of MITS college"}
    ]
)

print(response.choices[0].message.content)