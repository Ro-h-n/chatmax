import openai
from urllib.request import urlopen
from bs4 import BeautifulSoup
import googleSerp as gs
import html2text
import requests
import json
import streamlit as st
openai.api_key = "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"
def Chat2(input):
    completions = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages= [{"role": "user", "content": input}])
    return completions.choices[0].message.content.strip()


def GenerateImages(input):
    # connect to stable diffusion API
    url = 'https://stablediffusionapi.com/api/v3/text2img'

    data = {
        "key": "zxVzKUBjTEPY640IkRI4SDeIL5E8NhDlqFEjGwHeBjlo6vFjJpgizgVV1mez",
        "prompt": input,
        "negative_prompt": "",
        "width": "512",
        "height": "512",
        "samples": "1",
        "num_inference_steps": "20",
        "seed": None,
        "guidance_scale": 7.5,
        "safety_checker": "yes",
        "webhook": None,
        "track_id": None
    }

    response = requests.post(url, json=data)
    JSONResult = json.loads(response.text)
    print("Generating Image...")
    imgURL = JSONResult["output"][0]
    return imgURL


# SearchTheWeb("learnwithhasan.com affiliate marketing")
# print(BitcoinPriceAnalysis())

st.title('ChatGPT Max Edition 2.0 🚀')
st.subheader(
    'Now, You Can Generate Images, Analyze Current Crypto Prices, and Search The Web With ChatGPT')

input = st.text_input("Prompt:", value="", max_chars=100, key=None,
                      type="default", help=None, autocomplete=None, on_change=None,
                      args=None, kwargs=None, placeholder="search the web for ...", disabled=False,
                      label_visibility="visible")



if st.button("Generate image"):
    with st.spinner('Generating Your Image...'):
        result = GenerateImages(input)
        st.image(result)
    st.success('Done!')
   
if st.button("Ask ChatGPT"):
    with st.spinner('Asking chatgpt...'):
        result = Chat2(input)
        st.text_area(result)
    st.success('Done!')



#print(GenerateImages("child flying in the sky"))
