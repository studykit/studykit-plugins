# CAMAdditiveContainer.isProtected Property

Parent Object: [CAMAdditiveContainer](CAMAdditiveContainer.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMAdditiveContainer.h>

## Description

Gets and sets the "protected" property value of the operation. Gets/sets true if the operation is protected.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMAdditiveContainer\_var" is a variable referencing a CAMAdditiveContainer object. |

"cAMAdditiveContainer\_var" is a variable referencing a CAMAdditiveContainer object. ```` ``` #include <Cam/CAM/CAMAdditiveContainer.h>  // Get the value of the property. boolean propertyValue = cAMAdditiveContainer_var->isProtected();  // Set the value of the property, where value_var is a boolean. bool returnValue = cAMAdditiveContainer_var->isProtected(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |