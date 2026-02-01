# UntrimFeatureInput.untrimLoopType Property

Parent Object: [UntrimFeatureInput](UntrimFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UntrimFeatureInput.h>

## Description

Gets the loop type to be untrimmed. This is only used when faces are being untrimmed and is ignored for loops.

## Syntax

* [Python](#Python)
* [C++](#C++)

"untrimFeatureInput\_var" is a variable referencing a UntrimFeatureInput object. |

"untrimFeatureInput\_var" is a variable referencing a UntrimFeatureInput object. ```` ``` #include <Fusion/Features/UntrimFeatureInput.h>  // Get the value of the property. UntrimLoopTypes propertyValue = untrimFeatureInput_var->untrimLoopType(); ``` ```` |

## Property Value

This is a read only property whose value is a [UntrimLoopTypes](UntrimLoopTypes.htm).

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |