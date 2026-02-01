# ReplaceFaceFeature.parentComponent Property

Parent Object: [ReplaceFaceFeature](ReplaceFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReplaceFaceFeature.h>

## Description

Returns the parent component that owns this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"replaceFaceFeature\_var" is a variable referencing a ReplaceFaceFeature object. |

"replaceFaceFeature\_var" is a variable referencing a ReplaceFaceFeature object. ```` ``` #include <Fusion/Features/ReplaceFaceFeature.h>  // Get the value of the property. Ptr<Component> propertyValue = replaceFaceFeature_var->parentComponent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |