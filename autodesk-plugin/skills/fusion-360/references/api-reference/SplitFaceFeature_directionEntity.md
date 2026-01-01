# SplitFaceFeature.directionEntity Property

Parent Object: [SplitFaceFeature](SplitFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitFaceFeature.h>

## Description

Gets the direction entity when the split type is along a vector. If the split type is not alongVectorSplitType this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitFaceFeature\_var" is a variable referencing a SplitFaceFeature object.  ```` ``` # Get the value of the property. propertyValue = splitFaceFeature_var.directionEntity ``` ```` |

"splitFaceFeature\_var" is a variable referencing a SplitFaceFeature object. ```` ``` #include <Fusion/Features/SplitFaceFeature.h>  // Get the value of the property. Ptr<Base> propertyValue = splitFaceFeature_var->directionEntity(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version May 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |