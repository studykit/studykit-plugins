# RuledSurfaceFeature.isSuppressed Property

Parent Object: [RuledSurfaceFeature](RuledSurfaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuledSurfaceFeature.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruledSurfaceFeature\_var" is a variable referencing a RuledSurfaceFeature object. |

"ruledSurfaceFeature\_var" is a variable referencing a RuledSurfaceFeature object. ```` ``` #include <Fusion/Features/RuledSurfaceFeature.h>  // Get the value of the property. boolean propertyValue = ruledSurfaceFeature_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = ruledSurfaceFeature_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |