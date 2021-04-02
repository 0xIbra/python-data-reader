**data_reader . mapper**

## Mapper

#### Table of Contents
 - [__init__()](#__init__)
 - [transform()](#transform)

#### Methods

#### __init__(mapping, ondata=None, onfinish=None)
Mapper constructor.

###### Parameters
 - `mapping` : string - **required**
 - `ondata`: callable  
    This callback function will be called on each data key retrieval.  
    This is useful when you want to change, alter or transform retrieved data.

 - `onfinish`: callable  
    This callback is called at the end of the process, when all of the keys from the provided `mapping` are retrieved.  
    This is useful to append more data, or perform other actions.


#### transform(data) : dict
Transforms the data with the mapping you've provided.

**@returns** `dict`

###### Parameters
 - `data` : dict - **required**  
    Source data object from where the mapper is gonna retrieve data.

--------------------------------------------------------------------------------
