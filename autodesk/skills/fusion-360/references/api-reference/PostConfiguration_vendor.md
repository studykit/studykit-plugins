# PostConfiguration.vendor Property

Parent Object: [PostConfiguration](PostConfiguration.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Post/PostConfiguration.h>

## Description

Gets the name of the vendor of the machine tool or controller this post configuration supports.

## Syntax

* [Python](#Python)
* [C++](#C++)

"postConfiguration\_var" is a variable referencing a PostConfiguration object. |

"postConfiguration\_var" is a variable referencing a PostConfiguration object. ```` ``` #include <Cam/Post/PostConfiguration.h>  // Get the value of the property. string propertyValue = postConfiguration_var->vendor(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |