from typing import List, Tuple

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="gemma3:latest",
    verbose=True,
    temperature=0.6,
    seed=13,
    validate_model_on_init=True,  # To verify if model is available locally
)

messages: List[Tuple] = [
    (
        "system",
        "You are an smart AI assistant who is capable of answering any \
     user queries",
    ),
    (
        "user",
        "hi my name is swaminathan , i am working as a machine learning \
     engineer",
    ),
]

messages.append(("user", "can you tell what is my profession is ?"))


results = llm.invoke(messages)
print(results.text)
