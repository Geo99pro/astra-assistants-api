# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class ModifyThreadRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ModifyThreadRequest - a model defined in OpenAPI

        metadata: The metadata of this ModifyThreadRequest [Optional].
    """

    metadata: Optional[Dict[str, Any]] = Field(alias="metadata", default=None)

ModifyThreadRequest.update_forward_refs()
