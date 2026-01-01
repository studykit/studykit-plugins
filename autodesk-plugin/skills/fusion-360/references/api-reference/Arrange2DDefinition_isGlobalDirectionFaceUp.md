# Arrange2DDefinition.isGlobalDirectionFaceUp Property

Parent Object: [Arrange2DDefinition](Arrange2DDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange2DDefinition.h>

## Description

Gets and sets the global direction for selected faces. When true, the components specified by selecting a face will be oriented such that the selection face will be oriented upward in the arrangement.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange2DDefinition\_var" is a variable referencing an Arrange2DDefinition object. |

"arrange2DDefinition\_var" is a variable referencing an Arrange2DDefinition object. ```` ``` #include <Fusion/Arrange/Arrange2DDefinition.h>  // Get the value of the property. boolean propertyValue = arrange2DDefinition_var->isGlobalDirectionFaceUp();  // Set the value of the property, where value_var is a boolean. bool returnValue = arrange2DDefinition_var->isGlobalDirectionFaceUp(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |