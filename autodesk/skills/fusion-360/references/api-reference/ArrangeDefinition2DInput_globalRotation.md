# ArrangeDefinition2DInput.globalRotation Property

Parent Object: [ArrangeDefinition2DInput](ArrangeDefinition2DInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeDefinition2DInput.h>

## Description

Gets and sets the global rotation type. This defaults to AllRotationsArrangeRotationType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeDefinition2DInput\_var" is a variable referencing an ArrangeDefinition2DInput object. |

"arrangeDefinition2DInput\_var" is a variable referencing an ArrangeDefinition2DInput object. ```` ``` #include <Fusion/Arrange/ArrangeDefinition2DInput.h>  // Get the value of the property. ArrangeRotationTypes propertyValue = arrangeDefinition2DInput_var->globalRotation();  // Set the value of the property, where value_var is an ArrangeRotationTypes. bool returnValue = arrangeDefinition2DInput_var->globalRotation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ArrangeRotationTypes](ArrangeRotationTypes.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |