# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.chat_completion_request_user_message_content import ChatCompletionRequestUserMessageContent


class ChatCompletionRequestUserMessage(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ChatCompletionRequestUserMessage - a model defined in OpenAPI

        content: The content of this ChatCompletionRequestUserMessage.
        role: The role of this ChatCompletionRequestUserMessage.
        name: The name of this ChatCompletionRequestUserMessage [Optional].
    """

    content: ChatCompletionRequestUserMessageContent = Field(alias="content")
    role: str = Field(alias="role")
    name: Optional[str] = Field(alias="name", default=None)

ChatCompletionRequestUserMessage.update_forward_refs()
