# RipFeatures.isValid Property

Parent Object: [RipFeatures](RipFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ripFeatures\_var" is a variable referencing a RipFeatures object. |

"ripFeatures\_var" is a variable referencing a RipFeatures object. ```` ``` #include <Fusion/SheetMetal/RipFeatures.h>  // Get the value of the property. boolean propertyValue = ripFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |