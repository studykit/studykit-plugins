# NCProgram.isProtected Property

Parent Object: [NCProgram](NCProgram.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCProgram.h>

## Description

Gets and sets the "protected" property value of the operation. Gets/sets true if the operation is protected.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCProgram\_var" is a variable referencing a NCProgram object. |

"nCProgram\_var" is a variable referencing a NCProgram object. ```` ``` #include <Cam/NCProgram/NCProgram.h>  // Get the value of the property. boolean propertyValue = nCProgram_var->isProtected();  // Set the value of the property, where value_var is a boolean. bool returnValue = nCProgram_var->isProtected(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |