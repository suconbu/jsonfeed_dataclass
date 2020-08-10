# jsonfeed_dataclasses

This is the class definitions which represents the structure of [JSON Feed](https://jsonfeed.org).  

## Class

* Feed  
  Represents a top-level of the feed.

* Item  
  Represents a each article/entry of feed.

* Person  
  Represents a person information that using in author field, etc.

* Element  
  Base class of Feed, Item and Parson class.  
  It has the conversion methods such as to dict/JSON.

## Example of use

Sample code:
```py
# sample.py

from jsonfeed import Feed, Item

# Create feed instance
feed = Feed(title="sample1", home_page_url="http://sample.org")

# Add items into the feed
for i in range(0, 100):
    feed.items.append(Item(id=f"item{i}", url=f"http://sample.org/item{i}/"))

# Output the feed as JSON
print(feed.to_json(indent=2))
```

Run the sample code:
```sh
$ ls
jsonfeed.py sample.py

$ ./sample.py
{
  "version": "https://jsonfeed.org/version/1.1",
  "title": "sample1",
  "home_page_url": "http://sample.org",
  "items": [
    {
      "id": "item1",
      "url": "http://sample.org/item1/"
    }
    ...
  ]
}
```

# License

CC0
