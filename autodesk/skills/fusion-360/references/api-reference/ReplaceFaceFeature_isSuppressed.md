# ReplaceFaceFeature.isSuppressed Property

Parent Object: [ReplaceFaceFeature](ReplaceFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReplaceFaceFeature.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"replaceFaceFeature\_var" is a variable referencing a ReplaceFaceFeature object. |

"replaceFaceFeature\_var" is a variable referencing a ReplaceFaceFeature object. ```` ``` #include <Fusion/Features/ReplaceFaceFeature.h>  // Get the value of the property. boolean propertyValue = replaceFaceFeature_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = replaceFaceFeature_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |