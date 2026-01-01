# PathPatternFeature.baseFeature Property

Parent Object: [PathPatternFeature](PathPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeature.h>

## Description

If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathPatternFeature\_var" is a variable referencing a PathPatternFeature object. |

"pathPatternFeature\_var" is a variable referencing a PathPatternFeature object. ```` ``` #include <Fusion/Features/PathPatternFeature.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = pathPatternFeature_var->baseFeature(); ``` ```` |

## Property Value

This is a read only property whose value is a [BaseFeature](BaseFeature.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |