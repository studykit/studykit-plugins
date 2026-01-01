# NCProgram.operationId Property

Parent Object: [NCProgram](NCProgram.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCProgram.h>

## Description

Returns the id of the operation. This id is unique as compared to the ids of all other operations in the document. This id will not change when changing the order or parent of the operation. This id will remain valid when the document is saved and reloaded.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCProgram\_var" is a variable referencing a NCProgram object. |

"nCProgram\_var" is a variable referencing a NCProgram object. ```` ``` #include <Cam/NCProgram/NCProgram.h>  // Get the value of the property. integer propertyValue = nCProgram_var->operationId(); ``` ```` |

## Property Value

This is a read only property whose value is an integer.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |