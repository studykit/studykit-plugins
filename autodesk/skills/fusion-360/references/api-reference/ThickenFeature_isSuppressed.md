# ThickenFeature.isSuppressed Property

Parent Object: [ThickenFeature](ThickenFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThickenFeature.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"thickenFeature\_var" is a variable referencing a ThickenFeature object. |

"thickenFeature\_var" is a variable referencing a ThickenFeature object. ```` ``` #include <Fusion/Features/ThickenFeature.h>  // Get the value of the property. boolean propertyValue = thickenFeature_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = thickenFeature_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |