# RipFeature.isSuppressed Property

Parent Object: [RipFeature](RipFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeature.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ripFeature\_var" is a variable referencing a RipFeature object. |

"ripFeature\_var" is a variable referencing a RipFeature object. ```` ``` #include <Fusion/SheetMetal/RipFeature.h>  // Get the value of the property. boolean propertyValue = ripFeature_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = ripFeature_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |