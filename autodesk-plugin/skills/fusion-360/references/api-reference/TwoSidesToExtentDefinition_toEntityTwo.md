# TwoSidesToExtentDefinition.toEntityTwo Property

Parent Object: [TwoSidesToExtentDefinition](TwoSidesToExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TwoSidesToExtentDefinition.h>

## Description

Gets and sets the entity that defines the extent on side two. The valid types of entities can vary depending on the type of feature this is being used with.

## Syntax

* [Python](#Python)
* [C++](#C++)

"twoSidesToExtentDefinition\_var" is a variable referencing a TwoSidesToExtentDefinition object. |

"twoSidesToExtentDefinition\_var" is a variable referencing a TwoSidesToExtentDefinition object. ```` ``` #include <Fusion/Features/TwoSidesToExtentDefinition.h>  // Get the value of the property. Ptr<Base> propertyValue = twoSidesToExtentDefinition_var->toEntityTwo();  // Set the value of the property, where value_var is a Base. bool returnValue = twoSidesToExtentDefinition_var->toEntityTwo(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |