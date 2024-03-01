# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.create_message_request import CreateMessageRequest


class CreateThreadRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CreateThreadRequest - a model defined in OpenAPI

        messages: The messages of this CreateThreadRequest [Optional].
        metadata: The metadata of this CreateThreadRequest [Optional].
    """

    messages: Optional[List[CreateMessageRequest]] = Field(alias="messages", default=None)
    metadata: Optional[Dict[str, Any]] = Field(alias="metadata", default=None)

CreateThreadRequest.update_forward_refs()
