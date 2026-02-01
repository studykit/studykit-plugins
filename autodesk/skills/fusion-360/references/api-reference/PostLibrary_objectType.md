# PostLibrary.objectType Property

Parent Object: [PostLibrary](PostLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Post/PostLibrary.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"postLibrary\_var" is a variable referencing a PostLibrary object.  ```` ``` # Get the value of the property. propertyValue = postLibrary_var.objectType ``` ```` |

"postLibrary\_var" is a variable referencing a PostLibrary object. ```` ``` #include <Cam/Post/PostLibrary.h>  // Get the value of the property. string propertyValue = postLibrary_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |