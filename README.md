# Generative AI Using Python 🤖

This repository has implementations of Generative AI use cases created using Large Language Models (LLM) and Small Langauge Models (SLM) with the use of Langchain and other frameworks/tools available in Python. 

## Pre-requisites 🏗️

- Python >= 3.12
- Conda (Anaconda/Miniforge)
- Ollama

## Environment Setup 🛠️

### Python environment and dependencies 

Create the virtual environment used for running the python code with the below command
```shell
conda create -p ./genai-env python=3.12 -y
```

This will creates a virtual environment within the current working directory that has python version set to 3.12, once created activate the environment.

```shell
conda activate ./genai-env
```

Install the required package dependencies using the provided requirements.txt file on the same virtual environment
```shell
pip install -r requirements.txt
```

### Ollama

This repository will use language models from Ollama, download and install the tool from it's official [site.](https://ollama.com/) Once installed , pull any of the open source language model using the CLI command given below from their [models library](https://ollama.com/search). 

```bash
ollama pull gemma3:latest
```

Once the model is pulled verify it's existence by executing
```bash
ollama list
```

### Environment Variables 

Use the provided `.env.template` file to create the .env file ensure it is present on this project root of this repository.

## References

* [Langchain-Ollama Documentation](https://docs.langchain.com/oss/python/integrations/providers/ollama)
* [Langchain-Ollama API Reference](https://reference.langchain.com/python/integrations/langchain_ollama/?_gl=1*w0defm*_gcl_au*ODAyMDkwNzcuMTc2MzQ5MjA3Nw..*_ga*MTQ5OTA0ODg1MS4xNzYzNDkyMDc3*_ga_47WX3HKKY2*czE3NjM0OTIwNzgkbzEkZzEkdDE3NjM0OTMyMjgkajYwJGwwJGgw)
