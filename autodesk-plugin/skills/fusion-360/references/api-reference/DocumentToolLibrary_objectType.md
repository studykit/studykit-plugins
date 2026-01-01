# DocumentToolLibrary.objectType Property

Parent Object: [DocumentToolLibrary](DocumentToolLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/DocumentToolLibrary.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentToolLibrary\_var" is a variable referencing a DocumentToolLibrary object.  ```` ``` # Get the value of the property. propertyValue = documentToolLibrary_var.objectType ``` ```` |

"documentToolLibrary\_var" is a variable referencing a DocumentToolLibrary object. ```` ``` #include <Cam/Tools/DocumentToolLibrary.h>  // Get the value of the property. string propertyValue = documentToolLibrary_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |