# ArrangeComponent.isDirectionFlipped Property

Parent Object: [ArrangeComponent](ArrangeComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeComponent.h>

## Description

Specifies if the direction is flipped from it's default direction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeComponent\_var" is a variable referencing an ArrangeComponent object.  ```` ``` # Get the value of the property. propertyValue = arrangeComponent_var.isDirectionFlipped  # Set the value of the property. arrangeComponent_var.isDirectionFlipped = propertyValue ``` ```` |

"arrangeComponent\_var" is a variable referencing an ArrangeComponent object. ```` ``` #include <Fusion/Arrange/ArrangeComponent.h>  // Get the value of the property. boolean propertyValue = arrangeComponent_var->isDirectionFlipped();  // Set the value of the property, where value_var is a boolean. bool returnValue = arrangeComponent_var->isDirectionFlipped(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |