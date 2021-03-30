**data_reader . readers . json_reader**

## JSONReader

#### Table of Contents
 - [__init__()](#__init__)
 - [iterate()](#iterate)

#### Methods

#### __init__()
JSONReader constructor.

###### Parameters
 - `file_path` : string
 - `arguments` : dict
    - `node_path`: string  
      When this argument is not specified, the reader will only parse the root item whether it is an array or a json object.


#### iterate()
Streams data with a python generator.

###### No parameters

--------------------------------------------------------------------------------
