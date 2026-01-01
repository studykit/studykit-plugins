# RefoldFeature.name Property

Parent Object: [RefoldFeature](RefoldFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RefoldFeature.h>

## Description

Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric).

## Syntax

* [Python](#Python)
* [C++](#C++)

"refoldFeature\_var" is a variable referencing a RefoldFeature object. |

"refoldFeature\_var" is a variable referencing a RefoldFeature object. ```` ``` #include <Fusion/SheetMetal/RefoldFeature.h>  // Get the value of the property. string propertyValue = refoldFeature_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = refoldFeature_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |