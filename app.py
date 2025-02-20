import streamlit as st
import pandas as pd
import yaml
import io
from openai import OpenAI
import json


with open("api_keys.json") as f:
    api_keys = json.load(f)


MODEL_NAME = "gpt-4o"
OPENAI_API_KEY  = api_keys.get("openai", "")

client = OpenAI(api_key=OPENAI_API_KEY)


def modify_content(prompt, content):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are an assistant that modifies YAML or CSV files based on user instructions."},
            {"role": "user", "content": f"Change file based on this prompt: {prompt}\n\n{content}"}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content.strip()


# Streamlit Interface
st.title("Future backend service POC")

# Upload file
doc_file = st.file_uploader("Upload your YAML or CSV file", type=["yaml", "yml", "csv"])

if doc_file:
    file_type = doc_file.name.split(".")[-1]

    if file_type in ["yaml", "yml"]:
        content = yaml.safe_load(doc_file)
        content_str = yaml.dump(content, default_flow_style=False)
    else:
        content = pd.read_csv(doc_file)
        content_str = content.to_csv(index=False)

    st.text_area("Current file", content_str, height=200)

    # User input
    prompt = st.text_area("What do you want to change within the file ?")

    if st.button("Change file"):
        modified_content = modify_content(prompt, content_str)

        st.text_area("Modified file", modified_content, height=200)

        # Generate file to dl
        output_file = io.BytesIO()
        output_file.write(modified_content.encode())
        output_file.seek(0)
        st.download_button("Download modified file", output_file, file_name=f"modified.{file_type}")
