# Langchain

This directory has source files that use langchain (a Python SDK) , used for interacting with an LLM and make them effecient by adding additional knowledge resources.

## Pre-requisites

The scripts in the directory will use models from OpenAI and Ollama parallely, if you have better computation capacity you can run any open source models locally using Ollama, otherwise get an API key generated in OpenAI platform.

Anyone can generate an API key from OpenAI platform, a user will be provided with $5 credit each month for accessing all the OpenAI models. The same cycle will be revised after every month. For organizations, getting the same sort of service through Azure OpenAI is advisable.

## OpenAI API Key

* Inorder to generate a OpenAI API Key , visit the https://platform.openai.com/api-keys and sign in with your account (Gmail/any other SSO).
* Once logged in you will be landed into the OpenAI platform homepage, from there redirect to the **API Keys** Page located in the left navigation bar.
* Click on generate a new key and give it a name, the key will be generated.
* Copy the key and place it into some familiar location (Note: This keys will not again viewed from the platform site, it's intended to be confidential , don't share this key or have them harcoded in any parts of your code base).
* The best practice could be having that inside a .env file located in your working directory so that your code can easily access it whenever it wants. Make sure this .env file is not pushed into your repository by mentioning the .env file in your .gitignore.
* Format for saving an OpenAI API Key in env file will be like the below mentioned
```
OPENAI_API_KEY="sk-********************"
```

or you can also make it as a environment variable using the below command

```bash
export OPENAI_API_KEY="sk-********************"
```
this will make the key active for the whole shell session , if you need it to be active for a long time then use
```
echo "OPENAI_API_KEY="sk-********************"" >> ~/.bashrc
```
