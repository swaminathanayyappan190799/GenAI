from langchain_ollama import ChatOllama

from langchain.messages import ToolMessage
from langchain.tools import tool
from typing import Dict


# Sample function used to demonstrate the tool calling in LLM's
@tool
def pull_employee_records(employee_name: str) -> Dict[str, str | int]:
    """
    Function used to get data about employee from the backend datastore

    Parameters
    ----------
        employee_name: str
            Name of the employee
    Returns
    -------
        Dict[str, str | int]
            Details of the employee
    """
    employee_records = {
        "swaminathan": {
            "Name": "Swaminathan Ayyappan",
            "Profession": "MLE",
            "Years of experience": 4,
        },
        "sanjay": {
            "Name": "Sanjay",
            "Profession": "Data engineer",
            "Years of experience": 3,
        },
    }
    return employee_records.get(employee_name)


llm = ChatOllama(
    model="gpt-oss:20b",
    verbose=True,
    temperature=0.6,
    seed=13,
    validate_model_on_init=True,  # To verify if model is available locally
).bind_tools([pull_employee_records])

# Asking query to the LLM model that uses the defined tool
results = llm.invoke("Get the details about the employee : swaminathan")

# If LLM decides to use the tool then it will get listed on tool_calls param
print(results)

if results.tool_calls:
    tool_call = results.tool_calls[0]

    tool_result = pull_employee_records.invoke(input=tool_call.get("args"))

    final_response = llm.invoke(
        [
            results,
            ToolMessage(tool_call_id=tool_call.get("id"),
                        content=str(tool_result)),
        ]
    )

    print(final_response.content)
