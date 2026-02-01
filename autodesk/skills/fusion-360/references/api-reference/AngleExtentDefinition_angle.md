# AngleExtentDefinition.angle Property

Parent Object: [AngleExtentDefinition](AngleExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/AngleExtentDefinition.h>

## Description

Gets the ModelParameter that defines the angle. The value of the angle can be edited by using the properties on the ModelParameter object to edit the parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"angleExtentDefinition\_var" is a variable referencing an AngleExtentDefinition object. |

"angleExtentDefinition\_var" is a variable referencing an AngleExtentDefinition object. ```` ``` #include <Fusion/Features/AngleExtentDefinition.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = angleExtentDefinition_var->angle(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |