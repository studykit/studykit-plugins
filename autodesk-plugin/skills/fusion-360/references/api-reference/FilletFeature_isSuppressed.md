# FilletFeature.isSuppressed Property

Parent Object: [FilletFeature](FilletFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletFeature.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletFeature\_var" is a variable referencing a FilletFeature object. |

"filletFeature\_var" is a variable referencing a FilletFeature object. ```` ``` #include <Fusion/Features/FilletFeature.h>  // Get the value of the property. boolean propertyValue = filletFeature_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = filletFeature_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |