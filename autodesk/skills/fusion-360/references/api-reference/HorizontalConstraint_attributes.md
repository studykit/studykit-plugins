# HorizontalConstraint.attributes Property

Parent Object: [HorizontalConstraint](HorizontalConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/HorizontalConstraint.h>

## Description

Returns the collection of attributes associated with this geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"horizontalConstraint\_var" is a variable referencing a HorizontalConstraint object. |

"horizontalConstraint\_var" is a variable referencing a HorizontalConstraint object. ```` ``` #include <Fusion/Sketch/HorizontalConstraint.h>  // Get the value of the property. Ptr<Attributes> propertyValue = horizontalConstraint_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |