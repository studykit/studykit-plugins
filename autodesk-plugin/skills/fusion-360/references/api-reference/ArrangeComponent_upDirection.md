# ArrangeComponent.upDirection Property

Parent Object: [ArrangeComponent](ArrangeComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeComponent.h>

## Description

Returns a vector that is the up direction of this ArrangeComponent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeComponent\_var" is a variable referencing an ArrangeComponent object. |

"arrangeComponent\_var" is a variable referencing an ArrangeComponent object. ```` ``` #include <Fusion/Arrange/ArrangeComponent.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = arrangeComponent_var->upDirection(); ``` ```` |

## Property Value

This is a read only property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |