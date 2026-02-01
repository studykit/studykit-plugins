# CombineFeatures.count Property

Parent Object: [CombineFeatures](CombineFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CombineFeatures.h>

## Description

The number of combine features in the collection. This property returns nothing in the case where the feature is non-parametric.

## Syntax

* [Python](#Python)
* [C++](#C++)

"combineFeatures\_var" is a variable referencing a CombineFeatures object. |

"combineFeatures\_var" is a variable referencing a CombineFeatures object. ```` ``` #include <Fusion/Features/CombineFeatures.h>  // Get the value of the property. uinteger propertyValue = combineFeatures_var->count(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |