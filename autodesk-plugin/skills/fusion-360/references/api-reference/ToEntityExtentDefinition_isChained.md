# ToEntityExtentDefinition.isChained Property

Parent Object: [ToEntityExtentDefinition](ToEntityExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ToEntityExtentDefinition.h>

## Description

Gets and sets whether connected faces to the input entity should also be used when calculating the extent or if the input entity should be extended. A value of true indicates that connected entities should be used.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toEntityExtentDefinition\_var" is a variable referencing a ToEntityExtentDefinition object. |

"toEntityExtentDefinition\_var" is a variable referencing a ToEntityExtentDefinition object. ```` ``` #include <Fusion/Features/ToEntityExtentDefinition.h>  // Get the value of the property. boolean propertyValue = toEntityExtentDefinition_var->isChained();  // Set the value of the property, where value_var is a boolean. bool returnValue = toEntityExtentDefinition_var->isChained(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |