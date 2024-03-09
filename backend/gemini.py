import google.generativeai as genai
import textwrap
import markdown

# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
newexplain={}



import PIL

def generate_image_explanations(Title, images_presence, file_paths, model,explanations):
    # List to store explanations
    # explanations = []

    # Iterate over the indices
    for i in range(len(images_presence)):
        title = Title[i].lower()
        if images_presence[i]:
            img = PIL.Image.open(file_paths[i])
            response = model.generate_content(["explain image which in this image", img], stream=True)
            response.resolve()
            # image_explanation = to_markdown(response.text)
            image_explanation = response.text

            # Append the image explanation to the existing explanation
            explanations.append(explanations[i] + str(image_explanation))

            print(title)
        else:
            explanations.append(explanations[i])
            print(title)
    
    return explanations

# Example usage:
# explanations = generate_image_explanations(Title, images_presence, file_paths, model,to_markdown)