# OffsetFacesFeature.baseFeature Property

Parent Object: [OffsetFacesFeature](OffsetFacesFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFacesFeature.h>

## Description

If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFacesFeature\_var" is a variable referencing an OffsetFacesFeature object. |

"offsetFacesFeature\_var" is a variable referencing an OffsetFacesFeature object. ```` ``` #include <Fusion/Features/OffsetFacesFeature.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = offsetFacesFeature_var->baseFeature(); ``` ```` |

## Property Value

This is a read only property whose value is a [BaseFeature](BaseFeature.htm).

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |