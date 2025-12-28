from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import (
    JsonOutputParser)
from data_models.chat_models import ModelOutputFormat


llm = ChatOllama(
    model="gemma3:latest",
    verbose=True,
    temperature=0.6,
    seed=13,
    validate_model_on_init=True,  # To verify if model is available locally
)

output_parser = JsonOutputParser(pydantic_object=ModelOutputFormat)

prompt_template = PromptTemplate(
    input_variables=["character_name"],
    partial_variables={
        "format_instructions": output_parser.get_format_instructions()},
    template="""
You are an expert in writing essay about fictional character : {character_name}
The details you are going to provide is truthful and you can mention their
reference is any movies, comics or any other sorts.
If the character is a real person then mention about
their real life achievements.
Give it on the output format : {format_instructions}"""
)

chain = prompt_template | llm | output_parser

response = chain.invoke({"character_name": "Robert Downey Jr"})
print(response)
print(type(response))
