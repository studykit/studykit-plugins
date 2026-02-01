# ArrangeDefinition2DInput.globalQuantity Property

Parent Object: [ArrangeDefinition2DInput](ArrangeDefinition2DInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeDefinition2DInput.h>

## Description

Gets and sets the global quantity, which is the default quantity value for components. This defaults to 1.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeDefinition2DInput\_var" is a variable referencing an ArrangeDefinition2DInput object.  ```` ``` # Get the value of the property. propertyValue = arrangeDefinition2DInput_var.globalQuantity  # Set the value of the property. arrangeDefinition2DInput_var.globalQuantity = propertyValue ``` ```` |

"arrangeDefinition2DInput\_var" is a variable referencing an ArrangeDefinition2DInput object. ```` ``` #include <Fusion/Arrange/ArrangeDefinition2DInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = arrangeDefinition2DInput_var->globalQuantity();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = arrangeDefinition2DInput_var->globalQuantity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |