import os
from langchain_community.llms.ctransformers import CTransformers


llm = CTransformers(
    model=f"models{os.sep}llama-2-7b.ggmlv3.q8_0.bin",
    model_type="llama"
    )

print(llm.invoke("Hi who are you"))
