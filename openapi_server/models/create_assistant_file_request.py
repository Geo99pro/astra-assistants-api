# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class CreateAssistantFileRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CreateAssistantFileRequest - a model defined in OpenAPI

        file_id: The file_id of this CreateAssistantFileRequest.
    """

    file_id: str = Field(alias="file_id")

CreateAssistantFileRequest.update_forward_refs()
