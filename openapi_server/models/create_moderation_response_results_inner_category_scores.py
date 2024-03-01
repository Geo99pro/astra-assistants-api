# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class CreateModerationResponseResultsInnerCategoryScores(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CreateModerationResponseResultsInnerCategoryScores - a model defined in OpenAPI

        hate: The hate of this CreateModerationResponseResultsInnerCategoryScores.
        hate_threatening: The hate_threatening of this CreateModerationResponseResultsInnerCategoryScores.
        harassment: The harassment of this CreateModerationResponseResultsInnerCategoryScores.
        harassment_threatening: The harassment_threatening of this CreateModerationResponseResultsInnerCategoryScores.
        self_harm: The self_harm of this CreateModerationResponseResultsInnerCategoryScores.
        self_harm_intent: The self_harm_intent of this CreateModerationResponseResultsInnerCategoryScores.
        self_harm_instructions: The self_harm_instructions of this CreateModerationResponseResultsInnerCategoryScores.
        sexual: The sexual of this CreateModerationResponseResultsInnerCategoryScores.
        sexual_minors: The sexual_minors of this CreateModerationResponseResultsInnerCategoryScores.
        violence: The violence of this CreateModerationResponseResultsInnerCategoryScores.
        violence_graphic: The violence_graphic of this CreateModerationResponseResultsInnerCategoryScores.
    """

    hate: float = Field(alias="hate")
    hate_threatening: float = Field(alias="hate/threatening")
    harassment: float = Field(alias="harassment")
    harassment_threatening: float = Field(alias="harassment/threatening")
    self_harm: float = Field(alias="self-harm")
    self_harm_intent: float = Field(alias="self-harm/intent")
    self_harm_instructions: float = Field(alias="self-harm/instructions")
    sexual: float = Field(alias="sexual")
    sexual_minors: float = Field(alias="sexual/minors")
    violence: float = Field(alias="violence")
    violence_graphic: float = Field(alias="violence/graphic")

CreateModerationResponseResultsInnerCategoryScores.update_forward_refs()
