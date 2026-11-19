from openai import AzureOpenAI
endpoint = "https://project25115-resource.services.ai.azure.com/"
api_key = "1KpC5N3S76nK55GTEJ3Oy0qPorsV2tYmoDeSOAUNDj0Hjc8C6bqqJQQJ99CKACE1PydXJ3w3AAAAACOGsTKZ"
deployment_name = "gpt-5-mini"
long_text = """Technology has become an essential part of our everyday lives. It has changed the way people communicate, learn, work, and entertain themselves. In today's modern world, almost everyone depends on technology in one way or another. Smartphones, computers, the internet, and various digital applications have made our lives easier and more convenient. Students can attend online classes, access educational materials, complete assignments, and learn new skills from anywhere in the world. Similarly, employees can work remotely, attend virtual meetings, and communicate with colleagues without travelling long distances. Technology has also brought significant improvements to healthcare, transportation, banking, agriculture, and business. People can now transfer money within seconds, book tickets online, order food, and access important information with just a few clicks. However, excessive use of technology can also create problems such as reduced physical activity, eye strain, lack of concentration, and dependence on digital devices. Therefore, it is important to use technology wisely and maintain a healthy balance between the digital world and real life. Technology itself is neither good nor bad; it depends on how we use it."""
#key phrase extraction from user content 

from openai import AzureOpenAI

# 1. Endpoint should be the "Endpoint" or "Target URI" found in the Azure portal
# Format is typically: https://<your-resource-name>.openai.azure.com/
# Or the new format: https://<your-resource-name>.services.ai.azure.com/
endpoint = "https://project25115-resource.services.ai.azure.com/"

# 2. API Key (please ensure it is not leaked)
api_key = "1KpC5N3S76nK55GTEJ3Oy0qPorsV2tYmoDeSOAUNDj0Hjc8C6bqqJQQJ99CKACE1PydXJ3w3AAAAACOGsTKZ"

# 3. Deployment Name: fill in the deployment name you set in Azure AI Foundry
# It may be different from the model name (gpt-5-mini), be sure to verify
deployment_name = "gpt-5-mini"  # Please confirm this is your deployment name

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
        {"role": "system", "content": "you are an text summarization assistant.  summarize the user content."},
        {"role": "user", "content": long_text}
    ]
)

print(response.choices[0].message.content)