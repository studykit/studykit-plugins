# UntrimFeature.nativeObject Property

Parent Object: [UntrimFeature](UntrimFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UntrimFeature.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"untrimFeature\_var" is a variable referencing a UntrimFeature object. |

"untrimFeature\_var" is a variable referencing a UntrimFeature object. ```` ``` #include <Fusion/Features/UntrimFeature.h>  // Get the value of the property. Ptr<UntrimFeature> propertyValue = untrimFeature_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [UntrimFeature](UntrimFeature.htm).

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |