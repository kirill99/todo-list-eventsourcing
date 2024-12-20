from abc import ABC, abstractmethod

from pydantic import BaseModel


class PaginatorParamsIn(BaseModel):
    with_paginate: bool = True
    items_per_page: int = 10
    offset: int = 1


class FormDataInSchema(ABC, BaseModel):
    @classmethod
    @abstractmethod
    def as_form(cls): raise NotImplementedError(
        'Определите as_form в %s.' % (cls))
