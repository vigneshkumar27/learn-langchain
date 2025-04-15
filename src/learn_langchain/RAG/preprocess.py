from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter,
                                      SentenceTransformersTokenTextSplitter,
                                      TextSplitter,
                                      TokenTextSplitter,
                                      MarkdownHeaderTextSplitter,
                                      RecursiveJsonSplitter)
from pathlib import Path
import tiktoken

file_path = Path.joinpath(Path(__file__).resolve().parent,"documents","terraform.txt")
with open(file_path) as file:
    content = file.read()
  
# ----------------- Length based chunking -------------
  #-----------------token based chunk ---------------------
# text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
#     encoding_name="cl100k_base", chunk_size=50, chunk_overlap=0
# )
# texts = text_splitter.split_text(content)

 #------------------------- charector based chunking ----------------------
 
# text_splitter = CharacterTextSplitter(
#     separator="\n\n",
#     chunk_size=100,
#     chunk_overlap=0,
#     length_function=len,
#     is_separator_regex=False,
# )

# chunks = text_splitter.split_text(content)

# print(chunks[0])

# -------------------------- text structured splitting ---------------------

# text_splitter = RecursiveCharacterTextSplitter(chunk_size=200,chunk_overlap=0)

# chunks = text_splitter.split_text(content)

# print(chunks[0])

# --------------------- document based splitter -----------------------

 # -----------------markdown splitter -------------------------
# readme_file = Path.joinpath(Path(__file__).resolve().parent,"documents","readme.md")
# with open(readme_file) as file:
#     content = file.read()
# headers_to_split_on = [
#     ("#", "Header 1"),
#     ("##", "Header 2"),
#     ("###", "Header 3"),
# ]
# readme_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)

# chunks = readme_splitter.split_text(content)

# print(chunks[0])

 # ----------------json splitter ------------------
 
# import json

# import requests

# This is a large nested json object and will be loaded as a python dict
# json_data = requests.get("https://api.smith.langchain.com/openapi.json").json()

# splitter = RecursiveJsonSplitter(max_chunk_size=300)

# json_chunks = splitter.split_json(json_data=json_data)

# for chunk in json_chunks[:3]:
#     print(chunk)

# encoder = tiktoken.get_encoding("cl100k_base")

# token = encoder.encode(texts[0])

# print(len(token))
