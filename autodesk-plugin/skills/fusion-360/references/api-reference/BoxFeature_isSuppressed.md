# BoxFeature.isSuppressed Property

Parent Object: [BoxFeature](BoxFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoxFeature.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boxFeature\_var" is a variable referencing a BoxFeature object. |

"boxFeature\_var" is a variable referencing a BoxFeature object. ```` ``` #include <Fusion/Features/BoxFeature.h>  // Get the value of the property. boolean propertyValue = boxFeature_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = boxFeature_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |