# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class MessageContentTextAnnotationsFileCitationObjectFileCitation(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    MessageContentTextAnnotationsFileCitationObjectFileCitation - a model defined in OpenAPI

        file_id: The file_id of this MessageContentTextAnnotationsFileCitationObjectFileCitation.
        quote: The quote of this MessageContentTextAnnotationsFileCitationObjectFileCitation.
    """

    file_id: str = Field(alias="file_id")
    quote: str = Field(alias="quote")

MessageContentTextAnnotationsFileCitationObjectFileCitation.update_forward_refs()
