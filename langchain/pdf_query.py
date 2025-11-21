from dotenv import load_dotenv
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain_text_splitters.character import CharacterTextSplitter

load_dotenv()

# Instantiating the LLM and embedding model from Ollama
llm = OllamaLLM(model="gemma3:latest", verbose=True, temperature=0.6, seed=13)

embeddings = OllamaEmbeddings(model="embeddinggemma:latest")

# Loading PDF data through PyPDF
raw_data = PyPDFLoader(file_path="data/virtus-user-manual-27nov23.pdf").load()

# Splitting text data
text_splitter = CharacterTextSplitter(separator="\n", chunk_size=400)

split_docs = text_splitter.split_documents(raw_data)


vector_store = FAISS.from_documents(documents=split_docs, embedding=embeddings)
# vector_store.save_local(folder_path="data", index_name="virtus_faiss_index")

vectors = vector_store.similarity_search(
    query="what is the ideal psi to be maintained for tyres of virtus", k=5
)

# Create a retriever from the FAISS vector store
retriever = vector_store.as_retriever()

# Build a conversational retrieval chain from the LLM and retriever
chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    return_source_documents=True,
)

resp = chain.invoke(
    {"question": "how central locking works in virtus", "chat_history": []}
)

print(resp)
