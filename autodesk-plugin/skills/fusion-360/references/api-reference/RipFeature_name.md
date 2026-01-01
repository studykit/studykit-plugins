# RipFeature.name Property

Parent Object: [RipFeature](RipFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeature.h>

## Description

Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric).

## Syntax

* [Python](#Python)
* [C++](#C++)

"ripFeature\_var" is a variable referencing a RipFeature object. |

"ripFeature\_var" is a variable referencing a RipFeature object. ```` ``` #include <Fusion/SheetMetal/RipFeature.h>  // Get the value of the property. string propertyValue = ripFeature_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = ripFeature_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |