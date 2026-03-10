from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_ollama.llms import OllamaLLM

llm = OllamaLLM(model="gemma3:latest", verbose=True, temperature=0.6, seed=13)

examples = [
    {"word": "bright", "opposite": "dark"},
    {"word": "day", "opposite": "night"},
]

prompt = FewShotPromptTemplate(
    input_variables=["word"],
    example_prompt=PromptTemplate(
        input_variables=["word", "opposite"],
        template="{word} -> {opposite}",
    ),
    examples=examples,
    prefix=(
        "You are provided with a few examples of words and their antonyms.\n"
        "Use the examples to determine the antonym for the user's input.\n\n"
        "Examples:"
    ),
    suffix="\nNow provide the antonym for: {word}",
)

chain = prompt | llm

results = chain.invoke("sad")

print(results.strip())
