# PostConfiguration.isValid Property

Parent Object: [PostConfiguration](PostConfiguration.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Post/PostConfiguration.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"postConfiguration\_var" is a variable referencing a PostConfiguration object. |

"postConfiguration\_var" is a variable referencing a PostConfiguration object. ```` ``` #include <Cam/Post/PostConfiguration.h>  // Get the value of the property. boolean propertyValue = postConfiguration_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |