# CAMFolder.operationId Property

Parent Object: [CAMFolder](CAMFolder.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMFolder.h>

## Description

Returns the id of the operation. This id is unique as compared to the ids of all other operations in the document. This id will not change when changing the order or parent of the operation. This id will remain valid when the document is saved and reloaded.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMFolder\_var" is a variable referencing a CAMFolder object. |

"cAMFolder\_var" is a variable referencing a CAMFolder object. ```` ``` #include <Cam/CAM/CAMFolder.h>  // Get the value of the property. integer propertyValue = cAMFolder_var->operationId(); ``` ```` |

## Property Value

This is a read only property whose value is an integer.

## Version

Introduced in version May 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |