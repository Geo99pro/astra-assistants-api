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




from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_server.models.create_fine_tuning_job_request_hyperparameters import CreateFineTuningJobRequestHyperparameters
from openapi_server.models.create_fine_tuning_job_request_model import CreateFineTuningJobRequestModel
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateFineTuningJobRequest(BaseModel):
    """
    CreateFineTuningJobRequest
    """ # noqa: E501
    model: CreateFineTuningJobRequestModel
    training_file: StrictStr = Field(description="The ID of an uploaded file that contains training data.  See [upload file](/docs/api-reference/files/upload) for how to upload a file.  Your dataset must be formatted as a JSONL file. Additionally, you must upload your file with the purpose `fine-tune`.  See the [fine-tuning guide](/docs/guides/fine-tuning) for more details. ")
    hyperparameters: Optional[CreateFineTuningJobRequestHyperparameters] = None
    suffix: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=40)]] = Field(default=None, description="A string of up to 18 characters that will be added to your fine-tuned model name.  For example, a `suffix` of \"custom-model-name\" would produce a model name like `ft:gpt-3.5-turbo:openai:custom-model-name:7p4lURel`. ")
    validation_file: Optional[StrictStr] = Field(default=None, description="The ID of an uploaded file that contains validation data.  If you provide this file, the data is used to generate validation metrics periodically during fine-tuning. These metrics can be viewed in the fine-tuning results file. The same data should not be present in both train and validation files.  Your dataset must be formatted as a JSONL file. You must upload your file with the purpose `fine-tune`.  See the [fine-tuning guide](/docs/guides/fine-tuning) for more details. ")
    __properties: ClassVar[List[str]] = ["model", "training_file", "hyperparameters", "suffix", "validation_file"]

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
        """Create an instance of CreateFineTuningJobRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hyperparameters
        if self.hyperparameters:
            _dict['hyperparameters'] = self.hyperparameters.to_dict()
        # set to None if suffix (nullable) is None
        # and model_fields_set contains the field
        if self.suffix is None and "suffix" in self.model_fields_set:
            _dict['suffix'] = None

        # set to None if validation_file (nullable) is None
        # and model_fields_set contains the field
        if self.validation_file is None and "validation_file" in self.model_fields_set:
            _dict['validation_file'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateFineTuningJobRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "model": CreateFineTuningJobRequestModel.from_dict(obj.get("model")) if obj.get("model") is not None else None,
            "training_file": obj.get("training_file"),
            "hyperparameters": CreateFineTuningJobRequestHyperparameters.from_dict(obj.get("hyperparameters")) if obj.get("hyperparameters") is not None else None,
            "suffix": obj.get("suffix"),
            "validation_file": obj.get("validation_file")
        })
        return _obj


