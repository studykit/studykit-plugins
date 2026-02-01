# ArrangeComponent.priority Property

Parent Object: [ArrangeComponent](ArrangeComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeComponent.h>

## Description

Specifies the nesting priority for this component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeComponent\_var" is a variable referencing an ArrangeComponent object.  ```` ``` # Get the value of the property. propertyValue = arrangeComponent_var.priority  # Set the value of the property. arrangeComponent_var.priority = propertyValue ``` ```` |

"arrangeComponent\_var" is a variable referencing an ArrangeComponent object. ```` ``` #include <Fusion/Arrange/ArrangeComponent.h>  // Get the value of the property. ArrangePriorities propertyValue = arrangeComponent_var->priority();  // Set the value of the property, where value_var is an ArrangePriorities. bool returnValue = arrangeComponent_var->priority(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ArrangePriorities](ArrangePriorities.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |