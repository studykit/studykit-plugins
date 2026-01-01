# HoleFeature.holePositionDefinition Property

Parent Object: [HoleFeature](HoleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeature.h>

## Description

Returns a HolePositionDefinition object that provides access to the information used to define the position of the hole. This returns null in the case where IsParametric is false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeature\_var" is a variable referencing a HoleFeature object. |

"holeFeature\_var" is a variable referencing a HoleFeature object. ```` ``` #include <Fusion/Features/HoleFeature.h>  // Get the value of the property. Ptr<HolePositionDefinition> propertyValue = holeFeature_var->holePositionDefinition(); ``` ```` |

## Property Value

This is a read only property whose value is a [HolePositionDefinition](HolePositionDefinition.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |