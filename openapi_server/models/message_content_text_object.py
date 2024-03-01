# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.message_content_text_object_text import MessageContentTextObjectText


class MessageContentTextObject(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    MessageContentTextObject - a model defined in OpenAPI

        type: The type of this MessageContentTextObject.
        text: The text of this MessageContentTextObject.
    """

    type: str = Field(alias="type")
    text: MessageContentTextObjectText = Field(alias="text")

MessageContentTextObject.update_forward_refs()
