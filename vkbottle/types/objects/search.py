from . import apps, base, groups, users
import typing
from enum import Enum
from ..base import BaseModel
from vkbottle.types import objects


class Hint(BaseModel):
    app: "apps.App" = None
    description: str = None
    _global: "base.BoolInt" = None
    group: "groups.Group" = None
    profile: "users.UserMin" = None
    section: "HintSection" = None
    type: "HintType" = None


class HintSection(Enum):
    groups = "groups"
    events = "events"
    publics = "publics"
    correspondents = "correspondents"
    people = "people"
    friends = "friends"
    mutual_friends = "mutual_friends"


class HintType(Enum):
    group = "group"
    profile = "profile"
    vk_app = "vk_app"
