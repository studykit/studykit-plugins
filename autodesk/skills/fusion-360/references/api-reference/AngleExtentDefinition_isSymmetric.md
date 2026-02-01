# AngleExtentDefinition.isSymmetric Property

Parent Object: [AngleExtentDefinition](AngleExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/AngleExtentDefinition.h>

## Description

Gets and sets if the angle extent is in one direction or symmetric. For a hole this property will always return false and setting it is ignored.

## Syntax

* [Python](#Python)
* [C++](#C++)

"angleExtentDefinition\_var" is a variable referencing an AngleExtentDefinition object. |

"angleExtentDefinition\_var" is a variable referencing an AngleExtentDefinition object. ```` ``` #include <Fusion/Features/AngleExtentDefinition.h>  // Get the value of the property. boolean propertyValue = angleExtentDefinition_var->isSymmetric();  // Set the value of the property, where value_var is a boolean. bool returnValue = angleExtentDefinition_var->isSymmetric(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |