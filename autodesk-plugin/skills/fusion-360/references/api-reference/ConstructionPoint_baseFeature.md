# ConstructionPoint.baseFeature Property

Parent Object: [ConstructionPoint](ConstructionPoint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPoint.h>

## Description

If this construction point is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPoint\_var" is a variable referencing a ConstructionPoint object. |

"constructionPoint\_var" is a variable referencing a ConstructionPoint object. ```` ``` #include <Fusion/Construction/ConstructionPoint.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = constructionPoint_var->baseFeature(); ``` ```` |

## Property Value

This is a read only property whose value is a [BaseFeature](BaseFeature.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |