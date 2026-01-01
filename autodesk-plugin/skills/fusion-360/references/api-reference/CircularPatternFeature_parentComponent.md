# CircularPatternFeature.parentComponent Property

Parent Object: [CircularPatternFeature](CircularPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CircularPatternFeature.h>

## Description

Returns the parent component that owns this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternFeature\_var" is a variable referencing a CircularPatternFeature object. |

"circularPatternFeature\_var" is a variable referencing a CircularPatternFeature object. ```` ``` #include <Fusion/Features/CircularPatternFeature.h>  // Get the value of the property. Ptr<Component> propertyValue = circularPatternFeature_var->parentComponent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |