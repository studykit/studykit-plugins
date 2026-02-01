# RefoldFeatures.isValid Property

Parent Object: [RefoldFeatures](RefoldFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RefoldFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"refoldFeatures\_var" is a variable referencing a RefoldFeatures object. |

"refoldFeatures\_var" is a variable referencing a RefoldFeatures object. ```` ``` #include <Fusion/SheetMetal/RefoldFeatures.h>  // Get the value of the property. boolean propertyValue = refoldFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |