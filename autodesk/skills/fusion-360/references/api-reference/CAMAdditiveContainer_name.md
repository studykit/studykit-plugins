# CAMAdditiveContainer.name Property

Parent Object: [CAMAdditiveContainer](CAMAdditiveContainer.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMAdditiveContainer.h>

## Description

Gets and sets the name of the operation as seen in the browser. This name is unique as compared to the names of all other operations in the document.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMAdditiveContainer\_var" is a variable referencing a CAMAdditiveContainer object. |

"cAMAdditiveContainer\_var" is a variable referencing a CAMAdditiveContainer object. ```` ``` #include <Cam/CAM/CAMAdditiveContainer.h>  // Get the value of the property. string propertyValue = cAMAdditiveContainer_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = cAMAdditiveContainer_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version July 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |