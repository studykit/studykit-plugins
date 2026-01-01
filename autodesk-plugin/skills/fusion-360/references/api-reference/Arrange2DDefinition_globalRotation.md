# Arrange2DDefinition.globalRotation Property

Parent Object: [Arrange2DDefinition](Arrange2DDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange2DDefinition.h>

## Description

Gets and sets the global rotation type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange2DDefinition\_var" is a variable referencing an Arrange2DDefinition object. |

"arrange2DDefinition\_var" is a variable referencing an Arrange2DDefinition object. ```` ``` #include <Fusion/Arrange/Arrange2DDefinition.h>  // Get the value of the property. ArrangeRotationTypes propertyValue = arrange2DDefinition_var->globalRotation();  // Set the value of the property, where value_var is an ArrangeRotationTypes. bool returnValue = arrange2DDefinition_var->globalRotation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ArrangeRotationTypes](ArrangeRotationTypes.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |