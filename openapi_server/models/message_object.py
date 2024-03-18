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
from typing_extensions import Annotated
from openapi_server.models.message_object_content_inner import MessageObjectContentInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MessageObject(BaseModel):
    """
    Represents a message within a [thread](/docs/api-reference/threads).
    """ # noqa: E501
    id: StrictStr = Field(description="The identifier, which can be referenced in API endpoints.")
    object: StrictStr = Field(description="The object type, which is always `thread.message`.")
    created_at: StrictInt = Field(description="The Unix timestamp (in seconds) for when the message was created.")
    thread_id: StrictStr = Field(description="The [thread](/docs/api-reference/threads) ID that this message belongs to.")
    role: StrictStr = Field(description="The entity that produced the message. One of `user` or `assistant`.")
    content: List[MessageObjectContentInner] = Field(description="The content of the message in array of text and/or images.")
    assistant_id: Optional[StrictStr] = Field(description="If applicable, the ID of the [assistant](/docs/api-reference/assistants) that authored this message.")
    run_id: Optional[StrictStr] = Field(description="If applicable, the ID of the [run](/docs/api-reference/runs) associated with the authoring of this message.")
    file_ids: Annotated[List[StrictStr], Field(max_length=10)] = Field(description="A list of [file](/docs/api-reference/files) IDs that the assistant should use. Useful for tools like retrieval and code_interpreter that can access files. A maximum of 10 files can be attached to a message.")
    metadata: Optional[Dict[str, Any]] = Field(description="metadata_description")
    __properties: ClassVar[List[str]] = ["id", "object", "created_at", "thread_id", "role", "content", "assistant_id", "run_id", "file_ids", "metadata"]

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('thread.message'):
            raise ValueError("must be one of enum values ('thread.message')")
        return value

    @field_validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('user', 'assistant'):
            raise ValueError("must be one of enum values ('user', 'assistant')")
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
        """Create an instance of MessageObject from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in content (list)
        _items = []
        if self.content:
            for _item in self.content:
                if _item:
                    _items.append(_item.to_dict())
            _dict['content'] = _items
        # set to None if assistant_id (nullable) is None
        # and model_fields_set contains the field
        if self.assistant_id is None and "assistant_id" in self.model_fields_set:
            _dict['assistant_id'] = None

        # set to None if run_id (nullable) is None
        # and model_fields_set contains the field
        if self.run_id is None and "run_id" in self.model_fields_set:
            _dict['run_id'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MessageObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "object": obj.get("object"),
            "created_at": obj.get("created_at"),
            "thread_id": obj.get("thread_id"),
            "role": obj.get("role"),
            "content": [MessageObjectContentInner.from_dict(_item) for _item in obj.get("content")] if obj.get("content") is not None else None,
            "assistant_id": obj.get("assistant_id"),
            "run_id": obj.get("run_id"),
            "file_ids": obj.get("file_ids"),
            "metadata": obj.get("metadata")
        })
        return _obj

