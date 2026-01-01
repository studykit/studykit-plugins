# UnstitchFeature.isSuppressed Property

Parent Object: [UnstitchFeature](UnstitchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UnstitchFeature.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unstitchFeature\_var" is a variable referencing a UnstitchFeature object. |

"unstitchFeature\_var" is a variable referencing a UnstitchFeature object. ```` ``` #include <Fusion/Features/UnstitchFeature.h>  // Get the value of the property. boolean propertyValue = unstitchFeature_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = unstitchFeature_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |