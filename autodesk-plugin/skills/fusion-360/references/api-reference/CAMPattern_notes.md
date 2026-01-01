# CAMPattern.notes Property

Parent Object: [CAMPattern](CAMPattern.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMPattern.h>

## Description

Gets and sets the notes of the operation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMPattern\_var" is a variable referencing a CAMPattern object. |

"cAMPattern\_var" is a variable referencing a CAMPattern object. ```` ``` #include <Cam/CAM/CAMPattern.h>  // Get the value of the property. string propertyValue = cAMPattern_var->notes();  // Set the value of the property, where value_var is a string. bool returnValue = cAMPattern_var->notes(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version May 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |