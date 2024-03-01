# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.chat_completion_request_message_content_part import ChatCompletionRequestMessageContentPart


class ChatCompletionRequestUserMessageContent(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ChatCompletionRequestUserMessageContent - a model defined in OpenAPI

    """


ChatCompletionRequestUserMessageContent.update_forward_refs()
