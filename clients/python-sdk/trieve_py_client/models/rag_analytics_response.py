# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.11.9
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from trieve_py_client.models.rag_query_response import RagQueryResponse
from trieve_py_client.models.rag_usage_graph_response import RAGUsageGraphResponse
from trieve_py_client.models.rag_usage_response import RAGUsageResponse
from pydantic import StrictStr, Field
from typing import Union, List, Optional, Dict
from typing_extensions import Literal, Self

RAGANALYTICSRESPONSE_ONE_OF_SCHEMAS = ["RAGUsageGraphResponse", "RAGUsageResponse", "RagQueryResponse"]

class RAGAnalyticsResponse(BaseModel):
    """
    RAGAnalyticsResponse
    """
    # data type: RagQueryResponse
    oneof_schema_1_validator: Optional[RagQueryResponse] = None
    # data type: RAGUsageResponse
    oneof_schema_2_validator: Optional[RAGUsageResponse] = None
    # data type: RAGUsageGraphResponse
    oneof_schema_3_validator: Optional[RAGUsageGraphResponse] = None
    actual_instance: Optional[Union[RAGUsageGraphResponse, RAGUsageResponse, RagQueryResponse]] = None
    one_of_schemas: List[str] = Field(default=Literal["RAGUsageGraphResponse", "RAGUsageResponse", "RagQueryResponse"])

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = RAGAnalyticsResponse.model_construct()
        error_messages = []
        match = 0
        # validate data type: RagQueryResponse
        if not isinstance(v, RagQueryResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RagQueryResponse`")
        else:
            match += 1
        # validate data type: RAGUsageResponse
        if not isinstance(v, RAGUsageResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RAGUsageResponse`")
        else:
            match += 1
        # validate data type: RAGUsageGraphResponse
        if not isinstance(v, RAGUsageGraphResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RAGUsageGraphResponse`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in RAGAnalyticsResponse with oneOf schemas: RAGUsageGraphResponse, RAGUsageResponse, RagQueryResponse. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in RAGAnalyticsResponse with oneOf schemas: RAGUsageGraphResponse, RAGUsageResponse, RagQueryResponse. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into RagQueryResponse
        try:
            instance.actual_instance = RagQueryResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RAGUsageResponse
        try:
            instance.actual_instance = RAGUsageResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RAGUsageGraphResponse
        try:
            instance.actual_instance = RAGUsageGraphResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into RAGAnalyticsResponse with oneOf schemas: RAGUsageGraphResponse, RAGUsageResponse, RagQueryResponse. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into RAGAnalyticsResponse with oneOf schemas: RAGUsageGraphResponse, RAGUsageResponse, RagQueryResponse. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], RAGUsageGraphResponse, RAGUsageResponse, RagQueryResponse]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())

