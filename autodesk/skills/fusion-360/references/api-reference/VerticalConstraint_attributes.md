# VerticalConstraint.attributes Property

Parent Object: [VerticalConstraint](VerticalConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/VerticalConstraint.h>

## Description

Returns the collection of attributes associated with this geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"verticalConstraint\_var" is a variable referencing a VerticalConstraint object. |

"verticalConstraint\_var" is a variable referencing a VerticalConstraint object. ```` ``` #include <Fusion/Sketch/VerticalConstraint.h>  // Get the value of the property. Ptr<Attributes> propertyValue = verticalConstraint_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |