# ArrangeDefinition2DInput.isPartInPartAllowed Property

Parent Object: [ArrangeDefinition2DInput](ArrangeDefinition2DInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeDefinition2DInput.h>

## Description

Gets and sets if parts can be nested within void areas of other parts. This defaults to true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeDefinition2DInput\_var" is a variable referencing an ArrangeDefinition2DInput object.  ```` ``` # Get the value of the property. propertyValue = arrangeDefinition2DInput_var.isPartInPartAllowed  # Set the value of the property. arrangeDefinition2DInput_var.isPartInPartAllowed = propertyValue ``` ```` |

"arrangeDefinition2DInput\_var" is a variable referencing an ArrangeDefinition2DInput object. ```` ``` #include <Fusion/Arrange/ArrangeDefinition2DInput.h>  // Get the value of the property. boolean propertyValue = arrangeDefinition2DInput_var->isPartInPartAllowed();  // Set the value of the property, where value_var is a boolean. bool returnValue = arrangeDefinition2DInput_var->isPartInPartAllowed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |