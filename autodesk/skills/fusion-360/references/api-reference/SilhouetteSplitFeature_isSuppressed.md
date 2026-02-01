# SilhouetteSplitFeature.isSuppressed Property

Parent Object: [SilhouetteSplitFeature](SilhouetteSplitFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SilhouetteSplitFeature.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"silhouetteSplitFeature\_var" is a variable referencing a SilhouetteSplitFeature object. |

"silhouetteSplitFeature\_var" is a variable referencing a SilhouetteSplitFeature object. ```` ``` #include <Fusion/Features/SilhouetteSplitFeature.h>  // Get the value of the property. boolean propertyValue = silhouetteSplitFeature_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = silhouetteSplitFeature_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |