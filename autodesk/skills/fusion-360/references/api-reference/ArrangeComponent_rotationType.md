# ArrangeComponent.rotationType Property

Parent Object: [ArrangeComponent](ArrangeComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeComponent.h>

## Description

Gets and sets the rotation type for this ArrangeComponent. This defaults to use the global rotation type defined for the arrangement.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeComponent\_var" is a variable referencing an ArrangeComponent object.  ```` ``` # Get the value of the property. propertyValue = arrangeComponent_var.rotationType  # Set the value of the property. arrangeComponent_var.rotationType = propertyValue ``` ```` |

"arrangeComponent\_var" is a variable referencing an ArrangeComponent object. ```` ``` #include <Fusion/Arrange/ArrangeComponent.h>  // Get the value of the property. ArrangeRotationTypes propertyValue = arrangeComponent_var->rotationType();  // Set the value of the property, where value_var is an ArrangeRotationTypes. bool returnValue = arrangeComponent_var->rotationType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ArrangeRotationTypes](ArrangeRotationTypes.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |