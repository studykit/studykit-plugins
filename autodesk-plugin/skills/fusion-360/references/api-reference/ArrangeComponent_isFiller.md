# ArrangeComponent.isFiller Property

Parent Object: [ArrangeComponent](ArrangeComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeComponent.h>

## Description

Specifies if this component will be used to fill any left over empty space in the available envelopes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeComponent\_var" is a variable referencing an ArrangeComponent object.  ```` ``` # Get the value of the property. propertyValue = arrangeComponent_var.isFiller  # Set the value of the property. arrangeComponent_var.isFiller = propertyValue ``` ```` |

"arrangeComponent\_var" is a variable referencing an ArrangeComponent object. ```` ``` #include <Fusion/Arrange/ArrangeComponent.h>  // Get the value of the property. boolean propertyValue = arrangeComponent_var->isFiller();  // Set the value of the property, where value_var is a boolean. bool returnValue = arrangeComponent_var->isFiller(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |