# Arrange2DDefinition.isPartInPartAllowed Property

Parent Object: [Arrange2DDefinition](Arrange2DDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange2DDefinition.h>

## Description

Gets and sets if parts can be nested within void areas of other parts.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange2DDefinition\_var" is a variable referencing an Arrange2DDefinition object.  ```` ``` # Get the value of the property. propertyValue = arrange2DDefinition_var.isPartInPartAllowed  # Set the value of the property. arrange2DDefinition_var.isPartInPartAllowed = propertyValue ``` ```` |

"arrange2DDefinition\_var" is a variable referencing an Arrange2DDefinition object. ```` ``` #include <Fusion/Arrange/Arrange2DDefinition.h>  // Get the value of the property. boolean propertyValue = arrange2DDefinition_var->isPartInPartAllowed();  // Set the value of the property, where value_var is a boolean. bool returnValue = arrange2DDefinition_var->isPartInPartAllowed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |