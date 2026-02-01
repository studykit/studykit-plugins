# HorizontalPointsConstraint.attributes Property

Parent Object: [HorizontalPointsConstraint](HorizontalPointsConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/HorizontalPointsConstraint.h>

## Description

Returns the collection of attributes associated with this geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"horizontalPointsConstraint\_var" is a variable referencing a HorizontalPointsConstraint object. |

"horizontalPointsConstraint\_var" is a variable referencing a HorizontalPointsConstraint object. ```` ``` #include <Fusion/Sketch/HorizontalPointsConstraint.h>  // Get the value of the property. Ptr<Attributes> propertyValue = horizontalPointsConstraint_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |