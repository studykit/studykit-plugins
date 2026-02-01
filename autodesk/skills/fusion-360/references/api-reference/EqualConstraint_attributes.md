# EqualConstraint.attributes Property

Parent Object: [EqualConstraint](EqualConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/EqualConstraint.h>

## Description

Returns the collection of attributes associated with this geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"equalConstraint\_var" is a variable referencing an EqualConstraint object. |

"equalConstraint\_var" is a variable referencing an EqualConstraint object. ```` ``` #include <Fusion/Sketch/EqualConstraint.h>  // Get the value of the property. Ptr<Attributes> propertyValue = equalConstraint_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |