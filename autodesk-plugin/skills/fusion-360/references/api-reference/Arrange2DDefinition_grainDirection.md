# Arrange2DDefinition.grainDirection Property

Parent Object: [Arrange2DDefinition](Arrange2DDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange2DDefinition.h>

## Description

Defines the angle of the grain direction of the envelope. An angle of 0 is in the X direction of the envelope. You can modify the value by using the properties on the returned ModelParameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange2DDefinition\_var" is a variable referencing an Arrange2DDefinition object.  ```` ``` # Get the value of the property. propertyValue = arrange2DDefinition_var.grainDirection ``` ```` |

"arrange2DDefinition\_var" is a variable referencing an Arrange2DDefinition object. ```` ``` #include <Fusion/Arrange/Arrange2DDefinition.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = arrange2DDefinition_var->grainDirection(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |