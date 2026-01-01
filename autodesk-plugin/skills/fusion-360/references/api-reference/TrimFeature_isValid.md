# TrimFeature.isValid Property

Parent Object: [TrimFeature](TrimFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TrimFeature.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"trimFeature\_var" is a variable referencing a TrimFeature object. |

"trimFeature\_var" is a variable referencing a TrimFeature object. ```` ``` #include <Fusion/Features/TrimFeature.h>  // Get the value of the property. boolean propertyValue = trimFeature_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |