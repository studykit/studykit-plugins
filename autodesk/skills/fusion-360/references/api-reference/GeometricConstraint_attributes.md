# GeometricConstraint.attributes Property

Parent Object: [GeometricConstraint](GeometricConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraint.h>

## Description

Returns the collection of attributes associated with this geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraint\_var" is a variable referencing a GeometricConstraint object. |

"geometricConstraint\_var" is a variable referencing a GeometricConstraint object. ```` ``` #include <Fusion/Sketch/GeometricConstraint.h>  // Get the value of the property. Ptr<Attributes> propertyValue = geometricConstraint_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |