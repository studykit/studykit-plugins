# MoveFeatureRotateDefinition.angle Property

Parent Object: [MoveFeatureRotateDefinition](MoveFeatureRotateDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatureRotateDefinition.h>

## Description

Gets the model parameter that controls the rotation angle. You can use properties on the returned ModelParameter object to edit the offset distance.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatureRotateDefinition\_var" is a variable referencing a MoveFeatureRotateDefinition object. |

"moveFeatureRotateDefinition\_var" is a variable referencing a MoveFeatureRotateDefinition object. ```` ``` #include <Fusion/Features/MoveFeatureRotateDefinition.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = moveFeatureRotateDefinition_var->angle(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |