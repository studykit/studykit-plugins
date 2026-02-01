# TorusFeature.isSuppressed Property

Parent Object: [TorusFeature](TorusFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TorusFeature.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"torusFeature\_var" is a variable referencing a TorusFeature object. |

"torusFeature\_var" is a variable referencing a TorusFeature object. ```` ``` #include <Fusion/Features/TorusFeature.h>  // Get the value of the property. boolean propertyValue = torusFeature_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = torusFeature_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |