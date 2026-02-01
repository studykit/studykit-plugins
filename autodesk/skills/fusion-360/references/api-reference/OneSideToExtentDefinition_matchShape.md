# OneSideToExtentDefinition.matchShape Property

Parent Object: [OneSideToExtentDefinition](OneSideToExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OneSideToExtentDefinition.h>

## Description

Specifies if the face should be extended or use adjacent faces if necessary to define the termination of the extrusion. When used for a revolve feature this is ignored and is always treated as true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"oneSideToExtentDefinition\_var" is a variable referencing an OneSideToExtentDefinition object. |

"oneSideToExtentDefinition\_var" is a variable referencing an OneSideToExtentDefinition object. ```` ``` #include <Fusion/Features/OneSideToExtentDefinition.h>  // Get the value of the property. boolean propertyValue = oneSideToExtentDefinition_var->matchShape();  // Set the value of the property, where value_var is a boolean. bool returnValue = oneSideToExtentDefinition_var->matchShape(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |