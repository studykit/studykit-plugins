# ConcentricConstraint.attributes Property

Parent Object: [ConcentricConstraint](ConcentricConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ConcentricConstraint.h>

## Description

Returns the collection of attributes associated with this geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"concentricConstraint\_var" is a variable referencing a ConcentricConstraint object. |

"concentricConstraint\_var" is a variable referencing a ConcentricConstraint object. ```` ``` #include <Fusion/Sketch/ConcentricConstraint.h>  // Get the value of the property. Ptr<Attributes> propertyValue = concentricConstraint_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |