# UntrimFeature.isValid Property

Parent Object: [UntrimFeature](UntrimFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UntrimFeature.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"untrimFeature\_var" is a variable referencing a UntrimFeature object. |

"untrimFeature\_var" is a variable referencing a UntrimFeature object. ```` ``` #include <Fusion/Features/UntrimFeature.h>  // Get the value of the property. boolean propertyValue = untrimFeature_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |