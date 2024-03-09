from openai import OpenAI
import os
def generate_explanations(Title, topic_name):
    # Initialize the OpenAI client with your secure API key
    client = OpenAI(api_key=os.environ.get('openai'))

    # List to store unique titles
    unique_titles = []

    # List to store explanations
    explanations = []

    # Iterate over the titles
    for i in Title:
        title = Title[i].lower()
        if title not in unique_titles:
            # Make API call only for unique titles
            print(title)
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"this topic is related to {topic_name}. Give me information about this explain {title}"}
                ]
            )
            explanation = completion.choices[0].message.content
            # Append the explanation to the list of explanations
            explanations.append(explanation)
            # Add the title to the list of unique titles
            unique_titles.append(title)
        else:
            # For repeated titles, append an empty string
            print("repeated" + title)
            explanations.append("")

    return explanations

# # Example usage:
# Title = {"1": "Title1", "2": "Title2", "3": "Title3"}  # Example Title dictionary
# topic_name = "Example Topic"  # Example topic name
# explanations = generate_explanations(Title, topic_name)
# print(explanations)  # Print explanations
