# OffsetConstraint.distance Property

Parent Object: [OffsetConstraint](OffsetConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/OffsetConstraint.h>

## Description

The current distance of the offset in centimeters. To change the offset you need to modify the value of the parameter associated with the dimension, which you can get using the dimension property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetConstraint\_var" is a variable referencing an OffsetConstraint object. |

"offsetConstraint\_var" is a variable referencing an OffsetConstraint object. ```` ``` #include <Fusion/Sketch/OffsetConstraint.h>  // Get the value of the property. double propertyValue = offsetConstraint_var->distance(); ``` ```` |

## Property Value

This is a read only property whose value is a double.

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |