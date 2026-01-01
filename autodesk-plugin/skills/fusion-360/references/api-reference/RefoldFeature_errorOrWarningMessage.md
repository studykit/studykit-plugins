# RefoldFeature.errorOrWarningMessage Property

Parent Object: [RefoldFeature](RefoldFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RefoldFeature.h>

## Description

Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string.

## Syntax

* [Python](#Python)
* [C++](#C++)

"refoldFeature\_var" is a variable referencing a RefoldFeature object. |

"refoldFeature\_var" is a variable referencing a RefoldFeature object. ```` ``` #include <Fusion/SheetMetal/RefoldFeature.h>  // Get the value of the property. string propertyValue = refoldFeature_var->errorOrWarningMessage(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |