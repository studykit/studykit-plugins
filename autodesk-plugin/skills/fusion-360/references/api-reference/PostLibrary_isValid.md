# PostLibrary.isValid Property

Parent Object: [PostLibrary](PostLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Post/PostLibrary.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"postLibrary\_var" is a variable referencing a PostLibrary object. |

"postLibrary\_var" is a variable referencing a PostLibrary object. ```` ``` #include <Cam/Post/PostLibrary.h>  // Get the value of the property. boolean propertyValue = postLibrary_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |