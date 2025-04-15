from langchain_text_splitters import CharacterTextSplitter
from pathlib import Path

filepath = Path.joinpath(Path(__file__).resolve().parent,"documents","terraform.txt")
# # This is a long document we can split up.
with open(filepath) as f:
        content = f.read()

text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=10,
    chunk_overlap=2,
    length_function=len,
    is_separator_regex=False,
)
texts = text_splitter.create_documents([content])
print(texts[0])
    