from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="gemma3:latest",
    verbose=True,
    temperature=0.6,
    seed=13,
    validate_model_on_init=True,  # To verify if model is available locally
)

results = llm.invoke("Tell me about Dr. A.P.J Abdul Kalam")
print(results.text)
