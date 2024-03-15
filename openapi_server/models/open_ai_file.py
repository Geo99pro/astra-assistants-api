# coding: utf-8

"""
    OpenAI API

    The OpenAI REST API. Please see https://platform.openai.com/docs/api-reference for more details.

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OpenAIFile(BaseModel):
    """
    The `File` object represents a document that has been uploaded to OpenAI.
    """ # noqa: E501
    id: StrictStr = Field(description="The file identifier, which can be referenced in the API endpoints.")
    bytes: StrictInt = Field(description="The size of the file, in bytes.")
    created_at: StrictInt = Field(description="The Unix timestamp (in seconds) for when the file was created.")
    filename: StrictStr = Field(description="The name of the file.")
    object: StrictStr = Field(description="The object type, which is always `file`.")
    purpose: StrictStr = Field(description="The intended purpose of the file. Supported values are `fine-tune`, `fine-tune-results`, `assistants`, and `assistants_output`.")
    status: StrictStr = Field(description="Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.")
    status_details: Optional[StrictStr] = Field(default=None, description="Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.")
    __properties: ClassVar[List[str]] = ["id", "bytes", "created_at", "filename", "object", "purpose", "status", "status_details"]

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('file'):
            raise ValueError("must be one of enum values ('file')")
        return value

    @field_validator('purpose')
    def purpose_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('fine-tune', 'fine-tune-results', 'assistants', 'assistants_output'):
            raise ValueError("must be one of enum values ('fine-tune', 'fine-tune-results', 'assistants', 'assistants_output')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('uploaded', 'processed', 'error'):
            raise ValueError("must be one of enum values ('uploaded', 'processed', 'error')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OpenAIFile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OpenAIFile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "bytes": obj.get("bytes"),
            "created_at": obj.get("created_at"),
            "filename": obj.get("filename"),
            "object": obj.get("object"),
            "purpose": obj.get("purpose"),
            "status": obj.get("status"),
            "status_details": obj.get("status_details")
        })
        return _obj


