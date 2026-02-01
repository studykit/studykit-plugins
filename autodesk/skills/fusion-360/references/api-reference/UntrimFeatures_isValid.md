# UntrimFeatures.isValid Property

Parent Object: [UntrimFeatures](UntrimFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UntrimFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"untrimFeatures\_var" is a variable referencing a UntrimFeatures object. |

"untrimFeatures\_var" is a variable referencing a UntrimFeatures object. ```` ``` #include <Fusion/Features/UntrimFeatures.h>  // Get the value of the property. boolean propertyValue = untrimFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |