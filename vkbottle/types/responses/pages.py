import typing
from ..base import BaseModel
from vkbottle.types import objects

Save = int


class SaveModel(BaseModel):
    response: Save = None


GetHistory = typing.List[objects.pages.WikipageHistory]


class GetHistoryModel(BaseModel):
    response: GetHistory = None


GetTitles = typing.List[objects.pages.Wikipage]


class GetTitlesModel(BaseModel):
    response: GetTitles = None


GetVersion = objects.pages.WikipageFull


class GetVersionModel(BaseModel):
    response: GetVersion = None


Get = objects.pages.WikipageFull


class GetModel(BaseModel):
    response: Get = None


ParseWiki = str


class ParseWikiModel(BaseModel):
    response: ParseWiki = None


SaveAccess = int


class SaveAccessModel(BaseModel):
    response: SaveAccess = None
