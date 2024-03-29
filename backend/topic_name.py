import os
from openai import OpenAI

def get_topic_name(T, text):
    # Initialize the OpenAI client with your secure API key
    client = OpenAI(api_key=os.environ.get('openai'))

    # Create completion request
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "give the name of the topic from this   " + T + "these are my keywords " + text}
        ]
    )

    # Extract topic name from completion response
    topic_name = completion.choices[0].message.content

    return topic_name


