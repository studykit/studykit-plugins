# SplitBodyFeature.splittingTool Property

Parent Object: [SplitBodyFeature](SplitBodyFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitBodyFeature.h>

## Description

Gets the entity that defines the splitting tool. The splitting tool is a single entity that can be either a solid body, open body, plane, sketch curve or face that partially or fully intersects the bodyToSplit.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitBodyFeature\_var" is a variable referencing a SplitBodyFeature object.  ```` ``` # Get the value of the property. propertyValue = splitBodyFeature_var.splittingTool ``` ```` |

"splitBodyFeature\_var" is a variable referencing a SplitBodyFeature object. ```` ``` #include <Fusion/Features/SplitBodyFeature.h>  // Get the value of the property. Ptr<Base> propertyValue = splitBodyFeature_var->splittingTool(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |