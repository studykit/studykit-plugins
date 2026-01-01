# ArrangeFeature.baseFeature Property

Parent Object: [ArrangeFeature](ArrangeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeFeature.h>

## Description

If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeFeature\_var" is a variable referencing an ArrangeFeature object. |

"arrangeFeature\_var" is a variable referencing an ArrangeFeature object. ```` ``` #include <Fusion/Arrange/ArrangeFeature.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = arrangeFeature_var->baseFeature(); ``` ```` |

## Property Value

This is a read only property whose value is a [BaseFeature](BaseFeature.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |