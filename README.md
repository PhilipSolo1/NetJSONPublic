# NetJSON
## Overview
The Library that loads JSON files from the internet.
## Docs
### Usage
`loadnetjson`:
Devription: Loads a JSON file from a URL
Arguments/Input: `loadnetjson(<URL>)`
Argument/Input Info: `<URL>` needs to be in format `http://example.com/file.json`
### Example
`from autojson import loadnetjson # import
url = input("enter url to json: ") # ask user for url
output = loadnetjson(url) # load json file from url
print(output) # return the output`
### Requirements
 - urllib3
### pslib module
`pslib.netjson`
## Contibutors
 - PhilipSolo1
