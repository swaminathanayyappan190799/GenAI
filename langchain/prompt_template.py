from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="gemma3:latest", verbose=True, temperature=0.6, seed=13)

prompt = """
You are an expert in writing essay about fictional character : {character_name}
The details you are going to provide is truthful and you can mention their
reference is any movies, comics or any other sorts.
If the character is a real person then mention about
their real life achievements."""

prompt_template = PromptTemplate(input_variables=["character_name"],
                                 template=prompt)
chain = prompt_template | llm

results = chain.invoke("Iron Man")

print(results)
