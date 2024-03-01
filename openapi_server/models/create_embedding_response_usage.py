# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class CreateEmbeddingResponseUsage(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CreateEmbeddingResponseUsage - a model defined in OpenAPI

        prompt_tokens: The prompt_tokens of this CreateEmbeddingResponseUsage.
        total_tokens: The total_tokens of this CreateEmbeddingResponseUsage.
    """

    prompt_tokens: int = Field(alias="prompt_tokens")
    total_tokens: int = Field(alias="total_tokens")

CreateEmbeddingResponseUsage.update_forward_refs()
