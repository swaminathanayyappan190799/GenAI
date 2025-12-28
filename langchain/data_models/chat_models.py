from pydantic import BaseModel, Field
from typing import Union


# An pydantic object model to represent an LLM output response
class ModelOutputFormat(BaseModel):
    name: str = Field(description="Full Name of the person")
    age: Union[int, None] = Field(description="Age of the person , if unknown \
                                give None")
    profession: str = Field(description="Profession of the person")
    well_known_for: str = Field(description="The person well known for, or \
                                mention their achievements")
