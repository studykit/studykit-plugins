# SplitFaceFeature.splitType Property

Parent Object: [SplitFaceFeature](SplitFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitFaceFeature.h>

## Description

Returns the type of split type currently defined. To change the split type, use one of the set methods.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitFaceFeature\_var" is a variable referencing a SplitFaceFeature object. |

"splitFaceFeature\_var" is a variable referencing a SplitFaceFeature object. ```` ``` #include <Fusion/Features/SplitFaceFeature.h>  // Get the value of the property. SplitFaceSplitTypes propertyValue = splitFaceFeature_var->splitType(); ``` ```` |

## Property Value

This is a read only property whose value is a [SplitFaceSplitTypes](SplitFaceSplitTypes.htm).

## Version

Introduced in version May 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |