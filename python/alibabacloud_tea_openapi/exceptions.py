# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.exceptions import ResponseException 
from typing import Dict, Any


class AlibabaCloudException(ResponseException):
    def __init__(
        self, 
        retry_after: int = None,
        name: str = None,
        stack: str = None,
        status_code: int = None,
        code: str = None,
        message: str = None,
        description: str = None,
        request_id: str = None,
    ):
        super().__init__(
            retry_after,
            name,
            stack,
        )
        self.status_code = status_code
        self.code = code
        self.message = message
        self.description = description
        self.request_id = request_id

class ClientException(AlibabaCloudException):
    def __init__(
        self, 
        status_code: int = None,
        code: str = None,
        message: str = None,
        description: str = None,
        request_id: str = None,
        retry_after: int = None,
        name: str = None,
        stack: str = None,
        access_denied_detail: Dict[str, Any] = None,
    ):
        super().__init__(
            status_code,
            code,
            message,
            description,
            request_id,
            retry_after,
            name,
            stack,
        )
        self.access_denied_detail = access_denied_detail

class ServerException(AlibabaCloudException):
    def __init__(
        self, 
        status_code: int = None,
        code: str = None,
        message: str = None,
        description: str = None,
        request_id: str = None,
        retry_after: int = None,
        name: str = None,
        stack: str = None,
    ):
        super().__init__(
            status_code,
            code,
            message,
            description,
            request_id,
            retry_after,
            name,
            stack,
        )

class ThrottlingException(AlibabaCloudException):
    def __init__(
        self, 
        status_code: int = None,
        code: str = None,
        message: str = None,
        description: str = None,
        request_id: str = None,
        name: str = None,
        stack: str = None,
        retry_after: int = None,
    ):
        super().__init__(
            status_code,
            code,
            message,
            description,
            request_id,
            name,
            stack,
        )
        self.retry_after = retry_after

