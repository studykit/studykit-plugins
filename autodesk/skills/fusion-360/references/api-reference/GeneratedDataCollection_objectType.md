# GeneratedDataCollection.objectType Property

Parent Object: [GeneratedDataCollection](GeneratedDataCollection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeneratedData/GeneratedDataCollection.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"generatedDataCollection\_var" is a variable referencing a GeneratedDataCollection object.  ```` ``` # Get the value of the property. propertyValue = generatedDataCollection_var.objectType ``` ```` |

"generatedDataCollection\_var" is a variable referencing a GeneratedDataCollection object. ```` ``` #include <Cam/GeneratedData/GeneratedDataCollection.h>  // Get the value of the property. string propertyValue = generatedDataCollection_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |