# TwoDistancesChamferEdgeSet.isFlipped Property

Parent Object: [TwoDistancesChamferEdgeSet](TwoDistancesChamferEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TwoDistancesChamferEdgeSet.h>

## Description

Gets and sets if the chamfer is flipped. This swaps the directions for distance one and two.

## Syntax

* [Python](#Python)
* [C++](#C++)

"twoDistancesChamferEdgeSet\_var" is a variable referencing a TwoDistancesChamferEdgeSet object.  ```` ``` # Get the value of the property. propertyValue = twoDistancesChamferEdgeSet_var.isFlipped  # Set the value of the property. twoDistancesChamferEdgeSet_var.isFlipped = propertyValue ``` ```` |

"twoDistancesChamferEdgeSet\_var" is a variable referencing a TwoDistancesChamferEdgeSet object. ```` ``` #include <Fusion/Features/TwoDistancesChamferEdgeSet.h>  // Get the value of the property. boolean propertyValue = twoDistancesChamferEdgeSet_var->isFlipped();  // Set the value of the property, where value_var is a boolean. bool returnValue = twoDistancesChamferEdgeSet_var->isFlipped(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |