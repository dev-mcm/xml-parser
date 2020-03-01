# xmpl-parser
Untangle evictions data using [untangle](https://github.com/stchris/untangle/blob/master/docs/index.rst)
(documentation [here](https://untangle.readthedocs.io/en/latest/))



```
pip install untangle
```

Create /data and /output folders for inputs and outpust respectively, then in untangle_xml.py set 
```
XML  = 'data/input_file_name.xml'
```
see shell_scripts.sh for methods to cut down the XML 1GB files to a smaller sample for testing