# ReverseNormalFeature.parentComponent Property

Parent Object: [ReverseNormalFeature](ReverseNormalFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReverseNormalFeature.h>

## Description

Returns the parent component that owns this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"reverseNormalFeature\_var" is a variable referencing a ReverseNormalFeature object. |

"reverseNormalFeature\_var" is a variable referencing a ReverseNormalFeature object. ```` ``` #include <Fusion/Features/ReverseNormalFeature.h>  // Get the value of the property. Ptr<Component> propertyValue = reverseNormalFeature_var->parentComponent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |