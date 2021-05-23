# Modular .env type framework
This is a modular Python .env type framework for servicing global variables through a package structure.
## Table of Contents
* [Format](#format)
## Format
The project will support any amount of .env files, pending that they start with .env. To have multiple files, use the syntax .env.a, all variables from that file will then be available with a "A" in front. I.e. APASSWORD.
All env files MUST be in the env folder, subfolders will not work.
Any errors encountered while loading env files will not be handled and will end up forwarded to the main program at runtime.
### File
You can define any variable here, they will all be available as fully capitalized global variables through importing the package, replace the XXX with plain text for the value of the variable.
```
USERNAME=XXX
PASSWORD=XXX
```
### Special Types
To identify a variable as an integer append INT to the beginning of the variable name. I.e. INTPASSWORD=XXX will be loaded as the PASSWORD variable and converted to an integer.
To identify a variable as JSON append JSON to the beginning of the variable name. I.e. JSONUSERS=XXX will be loaded into JSON as the variable USERS. IMPORTANT NOTE: Do NOT include the " or ' at the beginning and end of the string or any newline characters, just the plain text content of the dumped string.