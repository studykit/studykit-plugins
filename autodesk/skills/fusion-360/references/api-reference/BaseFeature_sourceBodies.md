# BaseFeature.sourceBodies Property

Parent Object: [BaseFeature](BaseFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BaseFeature.h>

## Description

Returns the B-Rep bodies owned by the base feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"baseFeature\_var" is a variable referencing a BaseFeature object.  ```` ``` # Get the value of the property. propertyValue = baseFeature_var.sourceBodies ``` ```` |

"baseFeature\_var" is a variable referencing a BaseFeature object. ```` ``` #include <Fusion/Features/BaseFeature.h>  // Get the value of the property. std::vector<Ptr<BRepBody>> propertyValue = baseFeature_var->sourceBodies(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [BRepBody](BRepBody.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |