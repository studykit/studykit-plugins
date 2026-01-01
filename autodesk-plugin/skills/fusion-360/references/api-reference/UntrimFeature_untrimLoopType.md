# UntrimFeature.untrimLoopType Property

Parent Object: [UntrimFeature](UntrimFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UntrimFeature.h>

## Description

Gets the loop type that was untrimmed. To change the trim type, use one of the redefine methods.

## Syntax

* [Python](#Python)
* [C++](#C++)

"untrimFeature\_var" is a variable referencing a UntrimFeature object. |

"untrimFeature\_var" is a variable referencing a UntrimFeature object. ```` ``` #include <Fusion/Features/UntrimFeature.h>  // Get the value of the property. UntrimLoopTypes propertyValue = untrimFeature_var->untrimLoopType(); ``` ```` |

## Property Value

This is a read only property whose value is a [UntrimLoopTypes](UntrimLoopTypes.htm).

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |