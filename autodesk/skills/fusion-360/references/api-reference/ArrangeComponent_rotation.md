# ArrangeComponent.rotation Property

Parent Object: [ArrangeComponent](ArrangeComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeComponent.h>

## Description

Gets and sets the rotation angle of this ArrangeComponent. The value is defined in Radians, is relative to the zero direction vector returned by the zeroDirectionVector property, and is in a counterclockwise direction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeComponent\_var" is a variable referencing an ArrangeComponent object.  ```` ``` # Get the value of the property. propertyValue = arrangeComponent_var.rotation  # Set the value of the property. arrangeComponent_var.rotation = propertyValue ``` ```` |

"arrangeComponent\_var" is a variable referencing an ArrangeComponent object. ```` ``` #include <Fusion/Arrange/ArrangeComponent.h>  // Get the value of the property. double propertyValue = arrangeComponent_var->rotation();  // Set the value of the property, where value_var is a double. bool returnValue = arrangeComponent_var->rotation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |