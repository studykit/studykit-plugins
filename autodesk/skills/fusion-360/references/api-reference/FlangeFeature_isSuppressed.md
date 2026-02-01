# FlangeFeature.isSuppressed Property

Parent Object: [FlangeFeature](FlangeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlangeFeature.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flangeFeature\_var" is a variable referencing a FlangeFeature object. |

"flangeFeature\_var" is a variable referencing a FlangeFeature object. ```` ``` #include <Fusion/SheetMetal/FlangeFeature.h>  // Get the value of the property. boolean propertyValue = flangeFeature_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = flangeFeature_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |