# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class ChatCompletionFunctions(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ChatCompletionFunctions - a model defined in OpenAPI

        description: The description of this ChatCompletionFunctions [Optional].
        name: The name of this ChatCompletionFunctions.
        parameters: The parameters of this ChatCompletionFunctions [Optional].
    """

    description: Optional[str] = Field(alias="description", default=None)
    name: str = Field(alias="name")
    parameters: Optional[Dict[str, Any]] = Field(alias="parameters", default=None)

ChatCompletionFunctions.update_forward_refs()
