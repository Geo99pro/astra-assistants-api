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
from openapi_server.models.create_chat_completion_stream_response_choices_inner import CreateChatCompletionStreamResponseChoicesInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateChatCompletionStreamResponse(BaseModel):
    """
    Represents a streamed chunk of a chat completion response returned by model, based on the provided input.
    """ # noqa: E501
    id: StrictStr = Field(description="A unique identifier for the chat completion. Each chunk has the same ID.")
    choices: List[CreateChatCompletionStreamResponseChoicesInner] = Field(description="A list of chat completion choices. Can be more than one if `n` is greater than 1.")
    created: StrictInt = Field(description="The Unix timestamp (in seconds) of when the chat completion was created. Each chunk has the same timestamp.")
    model: StrictStr = Field(description="The model to generate the completion.")
    system_fingerprint: Optional[StrictStr] = Field(default=None, description="This fingerprint represents the backend configuration that the model runs with. Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism. ")
    object: StrictStr = Field(description="The object type, which is always `chat.completion.chunk`.")
    __properties: ClassVar[List[str]] = ["id", "choices", "created", "model", "system_fingerprint", "object"]

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('chat.completion.chunk'):
            raise ValueError("must be one of enum values ('chat.completion.chunk')")
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
        """Create an instance of CreateChatCompletionStreamResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in choices (list)
        _items = []
        if self.choices:
            for _item in self.choices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['choices'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateChatCompletionStreamResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "choices": [CreateChatCompletionStreamResponseChoicesInner.from_dict(_item) for _item in obj.get("choices")] if obj.get("choices") is not None else None,
            "created": obj.get("created"),
            "model": obj.get("model"),
            "system_fingerprint": obj.get("system_fingerprint"),
            "object": obj.get("object")
        })
        return _obj


