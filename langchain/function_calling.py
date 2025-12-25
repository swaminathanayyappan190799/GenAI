from langchain_ollama import ChatOllama

from langchain.messages import ToolMessage
from langchain.tools import tool


# Sample function used to demonstrate the tool calling in LLM's
@tool
def pull_student_records(student_name: str) -> str:
    """
    Function used to get data about student from the backend datastore

    Parameters
    ----------
        student_name: str
            Name of the student
    Returns
    -------
        str
            Department of the student
    """
    student_records = {
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
    return student_records.get(student_name)


llm = ChatOllama(
    model="gpt-oss:20b",
    verbose=True,
    temperature=0.6,
    seed=13,
    validate_model_on_init=True,  # To verify if model is available locally
).bind_tools([pull_student_records])

# Asking query to the LLM model that uses the defined tool
results = llm.invoke("Get the details about the student : swaminathan")

# If LLM decides to use the tool then it will get listed on tool_calls param
print(results)

if results.tool_calls:
    tool_call = results.tool_calls[0]

    tool_result = pull_student_records.invoke(input=tool_call.get("args"))

    final_response = llm.invoke(
        [
            results,
            ToolMessage(tool_call_id=tool_call.get("id"),
                        content=str(tool_result)),
        ]
    )

    print(final_response.content)
