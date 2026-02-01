# VerticalPointsConstraint.attributes Property

Parent Object: [VerticalPointsConstraint](VerticalPointsConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/VerticalPointsConstraint.h>

## Description

Returns the collection of attributes associated with this geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"verticalPointsConstraint\_var" is a variable referencing a VerticalPointsConstraint object. |

"verticalPointsConstraint\_var" is a variable referencing a VerticalPointsConstraint object. ```` ``` #include <Fusion/Sketch/VerticalPointsConstraint.h>  // Get the value of the property. Ptr<Attributes> propertyValue = verticalPointsConstraint_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |