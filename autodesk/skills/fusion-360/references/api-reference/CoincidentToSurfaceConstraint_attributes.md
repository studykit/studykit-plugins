# CoincidentToSurfaceConstraint.attributes Property

Parent Object: [CoincidentToSurfaceConstraint](CoincidentToSurfaceConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CoincidentToSurfaceConstraint.h>

## Description

Returns the collection of attributes associated with this geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coincidentToSurfaceConstraint\_var" is a variable referencing a CoincidentToSurfaceConstraint object. |

"coincidentToSurfaceConstraint\_var" is a variable referencing a CoincidentToSurfaceConstraint object. ```` ``` #include <Fusion/Sketch/CoincidentToSurfaceConstraint.h>  // Get the value of the property. Ptr<Attributes> propertyValue = coincidentToSurfaceConstraint_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |