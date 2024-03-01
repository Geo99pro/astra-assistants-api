# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.open_ai_file import OpenAIFile


class ListFilesResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ListFilesResponse - a model defined in OpenAPI

        data: The data of this ListFilesResponse.
        object: The object of this ListFilesResponse.
    """

    data: List[OpenAIFile] = Field(alias="data")
    object: str = Field(alias="object")

ListFilesResponse.update_forward_refs()
