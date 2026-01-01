# ArrangeComponent.occurrence Property

Parent Object: [ArrangeComponent](ArrangeComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeComponent.h>

## Description

Returns the Occurrence associated with this ArrangeComponent. If an Occurrence was used to define this ArrangeComponent, this will return the same thing as the occurrenceOrFace. If a BRepFace was used to define this ArrangeComponent, this will return the Occurrence the face is in. This is a convenience property to make accessing the occurrence simpler.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeComponent\_var" is a variable referencing an ArrangeComponent object. |

"arrangeComponent\_var" is a variable referencing an ArrangeComponent object. ```` ``` #include <Fusion/Arrange/ArrangeComponent.h>  // Get the value of the property. Ptr<Occurrence> propertyValue = arrangeComponent_var->occurrence(); ``` ```` |

## Property Value

This is a read only property whose value is an [Occurrence](Occurrence.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |