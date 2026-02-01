# FeatureList.isValid Property

Parent Object: [FeatureList](FeatureList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FeatureList.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"featureList\_var" is a variable referencing a FeatureList object. |

"featureList\_var" is a variable referencing a FeatureList object. ```` ``` #include <Fusion/Features/FeatureList.h>  // Get the value of the property. boolean propertyValue = featureList_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |