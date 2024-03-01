# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class ChatCompletionRequestMessageContentPartText(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ChatCompletionRequestMessageContentPartText - a model defined in OpenAPI

        type: The type of this ChatCompletionRequestMessageContentPartText.
        text: The text of this ChatCompletionRequestMessageContentPartText.
    """

    type: str = Field(alias="type")
    text: str = Field(alias="text")

ChatCompletionRequestMessageContentPartText.update_forward_refs()
