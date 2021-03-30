**data_reader . readers . xml_reader**

## XMLReader

#### Table of Contents
 - [__init__()](#__init__)
 - [iterate()](#iterate)

#### Methods

#### __init__()
XMLReader constructor.

###### Parameters
 - `file_path` : string
 - `arguments` : dict
    - `tag_path`: string  
      Path of the tags you want to read


#### iterate()
Streams data with a python generator.

###### No parameters



--------------------------------------------------------------------------------

Usage examples
--------------

Read data from xml file
```python
from data_reader import XMLReader

args = {
  'tag_path': 'after_root_tag/datapoint' # Required argument
}
reader = XMLReader('data/input_file.xml', arguments=args)
generator = reader.iterate()

for object in generator:
  pass # Your logic

```
