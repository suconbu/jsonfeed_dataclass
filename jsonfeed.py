#!/usr/bin/env python3

# This is the class definitions which represents the structure of (https://jsonfeed.org)

import json
import dataclasses
from typing import List
from datetime import datetime

@dataclasses.dataclass
class Element:
    def to_dict(self, skip_none=True):
        d = dataclasses.asdict(self)
        return self.__filter_none(d) if skip_none else d

    def to_json(self, indent=None, ensure_ascii=False, skip_none=True):
        return json.dumps(self.to_dict(skip_none=skip_none), indent=indent, ensure_ascii=ensure_ascii, default=self.__json_default)

    def __filter_none(self, obj) -> dict:
        if isinstance(obj, dict):
            items = map(lambda item: (item[0], self.__filter_none(item[1])), obj.items())
            return {k: v for k, v in items if v is not None}
        elif isinstance(obj, list):
            return list(self.__filter_none(v) for v in obj) if obj else None
        elif isinstance(obj, tuple):
            return tuple(self.__filter_none(v) for v in obj) if obj else None
        else:
            return obj

    def __json_default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError()

@dataclasses.dataclass
class Person(Element):
    name: str
    url: str = dataclasses.field(default=None)
    avatar: str = dataclasses.field(default=None)

@dataclasses.dataclass
class Attachment(Element):
    url: str
    mime_type: str
    title: str = dataclasses.field(default=None)
    size_in_bytes: int = dataclasses.field(default=None)
    duration_in_seconds: int = dataclasses.field(default=None)

@dataclasses.dataclass
class Item(Element):
    id: str
    url: str = dataclasses.field(default=None)
    external_url: str = dataclasses.field(default=None)
    title: str = dataclasses.field(default=None)
    content_html: str = dataclasses.field(default=None)
    content_text: str = dataclasses.field(default=None)
    summary: str = dataclasses.field(default=None)
    image: str = dataclasses.field(default=None)
    banner_image: str = dataclasses.field(default=None)
    date_published: datetime = dataclasses.field(default=None)
    date_modified: datetime = dataclasses.field(default=None)
    authors: List[Person] = dataclasses.field(default_factory=list)
    tags: List[str] = dataclasses.field(default_factory=list)
    language: str = dataclasses.field(default=None)
    attachments: List[Attachment] = dataclasses.field(default_factory=list)

@dataclasses.dataclass
class Feed(Element):
    version: str = dataclasses.field(default="https://jsonfeed.org/version/1.1", init=False)
    title: str
    home_page_url: str = dataclasses.field(default=None)
    feed_url: str = dataclasses.field(default=None)
    description: str = dataclasses.field(default=None)
    user_comment: str = dataclasses.field(default=None)
    next_url: str = dataclasses.field(default=None)
    icon: str = dataclasses.field(default=None)
    favicon: str = dataclasses.field(default=None)
    authors: List[Person] = dataclasses.field(default_factory=list)
    next_url: str = dataclasses.field(default=None)
    language: str = dataclasses.field(default=None)
    expired: bool = dataclasses.field(default=None)
    hubs: List[object] = dataclasses.field(default_factory=list)
    items: List[Item] = dataclasses.field(default_factory=list)

def exsample_of_use():
    feed = Feed(title="sample1", home_page_url="http://sample.org")

    for i in range(0, 10):
        feed.items.append(Item(id=f"item{i}", url=f"http://sample.org/item{i}/"))

    print(feed.to_json(indent=2))

if __name__ == "__main__":
    exsample_of_use()
