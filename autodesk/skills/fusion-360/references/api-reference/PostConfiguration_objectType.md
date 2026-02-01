# PostConfiguration.objectType Property

Parent Object: [PostConfiguration](PostConfiguration.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Post/PostConfiguration.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"postConfiguration\_var" is a variable referencing a PostConfiguration object.  ```` ``` # Get the value of the property. propertyValue = postConfiguration_var.objectType ``` ```` |

"postConfiguration\_var" is a variable referencing a PostConfiguration object. ```` ``` #include <Cam/Post/PostConfiguration.h>  // Get the value of the property. string propertyValue = postConfiguration_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |