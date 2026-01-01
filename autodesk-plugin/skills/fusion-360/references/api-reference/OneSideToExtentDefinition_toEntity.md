# OneSideToExtentDefinition.toEntity Property

Parent Object: [OneSideToExtentDefinition](OneSideToExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OneSideToExtentDefinition.h>

## Description

Gets and sets the entity that defines the extent. The valid types of entities can vary depending on the type of feature this is being used with.

## Syntax

* [Python](#Python)
* [C++](#C++)

"oneSideToExtentDefinition\_var" is a variable referencing an OneSideToExtentDefinition object. |

"oneSideToExtentDefinition\_var" is a variable referencing an OneSideToExtentDefinition object. ```` ``` #include <Fusion/Features/OneSideToExtentDefinition.h>  // Get the value of the property. Ptr<Base> propertyValue = oneSideToExtentDefinition_var->toEntity();  // Set the value of the property, where value_var is a Base. bool returnValue = oneSideToExtentDefinition_var->toEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |