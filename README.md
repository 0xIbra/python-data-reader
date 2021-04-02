[Data Reader](https://github.com/polkovnik-z/python-data-reader/blob/master/README.md)
===========
> Python package that **lazily** reads data from large **JSON**, **XML** and **CSV** files.

Why not use the already existing libs you ask ?  
Well, for me, it was crucial to have a small package size that can be deployed to a **Serverless** environment as this was the main goal.  

This package has only one dependency, and that is `ijson` which itself is small.

Installation
------------
```sh
pip install data-reader
```

API Reference
-------------
 * [Mapper](https://github.com/polkovnik-z/python-data-reader/blob/master/docs/mapper.md)
 * Readers
   * [CSVReader - `data_reader.readers.csv_reader`](https://github.com/polkovnik-z/python-data-reader/blob/master/docs/csv-reader.md)
   * [JSONReader - `data_reader.readers.json_reader`](https://github.com/polkovnik-z/python-data-reader/blob/master/docs/json-reader.md)
   * [XMLReader - `data_reader.readers.xml_reader`](https://github.com/polkovnik-z/python-data-reader/blob/master/docs/xm-reader.md)
