# ArrangeDefinition2DInput.isGlobalDirectionFaceUp Property

Parent Object: [ArrangeDefinition2DInput](ArrangeDefinition2DInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeDefinition2DInput.h>

## Description

Gets and sets the global direction for input faces. When true, the components specified by selecting a face will be oriented such that the selection face will be oriented upward in the arrangement. This defaults to true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeDefinition2DInput\_var" is a variable referencing an ArrangeDefinition2DInput object. |

"arrangeDefinition2DInput\_var" is a variable referencing an ArrangeDefinition2DInput object. ```` ``` #include <Fusion/Arrange/ArrangeDefinition2DInput.h>  // Get the value of the property. boolean propertyValue = arrangeDefinition2DInput_var->isGlobalDirectionFaceUp();  // Set the value of the property, where value_var is a boolean. bool returnValue = arrangeDefinition2DInput_var->isGlobalDirectionFaceUp(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |