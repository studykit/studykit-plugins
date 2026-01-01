# ArrangeComponent.quantity Property

Parent Object: [ArrangeComponent](ArrangeComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeComponent.h>

## Description

Specifies the quantity of this component to use in the arrange. This defaults to -1, which indicates that the global quantity is to be used.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeComponent\_var" is a variable referencing an ArrangeComponent object.  ```` ``` # Get the value of the property. propertyValue = arrangeComponent_var.quantity  # Set the value of the property. arrangeComponent_var.quantity = propertyValue ``` ```` |

"arrangeComponent\_var" is a variable referencing an ArrangeComponent object. ```` ``` #include <Fusion/Arrange/ArrangeComponent.h>  // Get the value of the property. integer propertyValue = arrangeComponent_var->quantity();  // Set the value of the property, where value_var is an integer. bool returnValue = arrangeComponent_var->quantity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |