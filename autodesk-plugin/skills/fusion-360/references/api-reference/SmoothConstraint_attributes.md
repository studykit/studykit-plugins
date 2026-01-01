# SmoothConstraint.attributes Property

Parent Object: [SmoothConstraint](SmoothConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SmoothConstraint.h>

## Description

Returns the collection of attributes associated with this geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"smoothConstraint\_var" is a variable referencing a SmoothConstraint object. |

"smoothConstraint\_var" is a variable referencing a SmoothConstraint object. ```` ``` #include <Fusion/Sketch/SmoothConstraint.h>  // Get the value of the property. Ptr<Attributes> propertyValue = smoothConstraint_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |