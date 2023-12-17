import google.generativeai as genai
import textwrap
from IPython.display import display, Markdown
from PIL import Image


# Setup your API key
with open('api.txt', 'r') as file:
    api_key = file.read().strip()

GOOGLE_API_KEY = api_key
genai.configure(api_key=GOOGLE_API_KEY)





def img(imgpath):
    if imgpath == 'no':
        img = 'n'
    else:
        img = Image.open('Images/' + imgpath)
        img
    return img







def GenAI(user_input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_input, stream=True)
    response.resolve()


    def to_markdown(text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
    
    formatted_response = to_markdown(response.text)

    return  response.text



def ImgGenAI(user_input, inp_image):
    image = img(inp_image)
    model = genai.GenerativeModel('gemini-pro-vision')
    chat = model.start_chat(history=[])
    chat
    response = model.generate_content([user_input, image], stream=True)
    response.resolve()

    def to_markdown(text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

    formatted_response = to_markdown(response.text)
    return  response.text





print('What Model Do You Want? ')
print('')
print('1 = Gemini-Pro')
print('2 = Gemini-pro-vision')
user = input('Select [1], or [2]:- ')

if user == '1':  # Compare with string '1' instead of integer 1
    while True:
        print('')
        multi_input = input('Gemini-Pro:- ')
        print('')
        if multi_input.lower() != 'exit':
            model_response = GenAI(multi_input)
            print('------------------------response start-----------------')
            print('')
            print(model_response)
            print('')
            print('--------------------------response end-------------------')
        else:
            break

elif user == '2':  # Compare with string '2' instead of integer 2
    while True:
        print('')
        user_input = input('Ask Gemini-Pro-Vision:- ')
        print('')
        image_name = input('Image Name:- ') 

        if user_input.lower() != 'exit':
            model_response = ImgGenAI(user_input, image_name)
            print('-------------------response start-----------------')
            print('')
            print(model_response)
            print('')
            print('----------------------response end----------------')
        else:
            break
else:
    print("Invalid input. Please select either [1] or [2].")
















# while True:
#     lines = input('Ask Gemenai:- ')

#     imagepath = input("Image path:- ")
#     image = img(imagepath)

#     if lines != 'exit':
#         print('---------Response start-------------')
#         print('')
#         print(Gemenai(lines, image))
#         print('')
#         print('------------Response end-------------')
#     else:
#         break







