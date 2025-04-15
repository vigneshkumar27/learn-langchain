from langchain_chroma import Chroma
from dotenv import load_dotenv
load_dotenv()

from uuid import uuid4

from langchain_openai import AzureOpenAIEmbeddings
from langchain_core.documents import Document
embedding_client = AzureOpenAIEmbeddings(model="text-embedding")

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embedding_client,
    persist_directory="./db"
)

# ----------------insert a sample data ---------------------------

# document1 = Document(
#     page_content="I have a bad feeling I am going to get deleted :(",
#     metadata={"source": "tweet"},
#     id=10,
# )
# documents=[document1]
# uuids = [str(uuid4()) for _ in range(len(documents))]

# vector_store.add_documents(documents=documents, ids=uuids)

results = vector_store.similarity_search(
    "LangChain provides abstractions to make working with LLMs easy",
    k=2,
)
for res in results:
    print(f"* {res.page_content} [{res.metadata}]")