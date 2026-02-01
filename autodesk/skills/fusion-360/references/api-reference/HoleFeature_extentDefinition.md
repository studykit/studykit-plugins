# HoleFeature.extentDefinition Property

Parent Object: [HoleFeature](HoleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeature.h>

## Description

Gets the definition object that is defining the extent of the hole. Modifying the definition object will cause the hole to recompute. The extent type of a hole is currently limited to a distance extent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeature\_var" is a variable referencing a HoleFeature object. |

"holeFeature\_var" is a variable referencing a HoleFeature object. ```` ``` #include <Fusion/Features/HoleFeature.h>  // Get the value of the property. Ptr<ExtentDefinition> propertyValue = holeFeature_var->extentDefinition(); ``` ```` |

## Property Value

This is a read only property whose value is an [ExtentDefinition](ExtentDefinition.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |