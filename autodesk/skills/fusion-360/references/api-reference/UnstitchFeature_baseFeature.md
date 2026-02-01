# UnstitchFeature.baseFeature Property

Parent Object: [UnstitchFeature](UnstitchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UnstitchFeature.h>

## Description

If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unstitchFeature\_var" is a variable referencing a UnstitchFeature object. |

"unstitchFeature\_var" is a variable referencing a UnstitchFeature object. ```` ``` #include <Fusion/Features/UnstitchFeature.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = unstitchFeature_var->baseFeature(); ``` ```` |

## Property Value

This is a read only property whose value is a [BaseFeature](BaseFeature.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |