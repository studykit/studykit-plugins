# FlangeFeature.name Property

Parent Object: [FlangeFeature](FlangeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlangeFeature.h>

## Description

Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric).

## Syntax

* [Python](#Python)
* [C++](#C++)

"flangeFeature\_var" is a variable referencing a FlangeFeature object. |

"flangeFeature\_var" is a variable referencing a FlangeFeature object. ```` ``` #include <Fusion/SheetMetal/FlangeFeature.h>  // Get the value of the property. string propertyValue = flangeFeature_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = flangeFeature_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |