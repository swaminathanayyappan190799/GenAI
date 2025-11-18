from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="gemma3:latest",
    verbose=True,
    temperature=0.6,
    seed=13,
    validate_model_on_init=True  # To verify if model is available locally
)

print(llm.invoke("Explain me about Iron man"))
