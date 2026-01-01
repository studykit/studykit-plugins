# BaseFeature.nativeObject Property

Parent Object: [BaseFeature](BaseFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BaseFeature.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"baseFeature\_var" is a variable referencing a BaseFeature object. |

"baseFeature\_var" is a variable referencing a BaseFeature object. ```` ``` #include <Fusion/Features/BaseFeature.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = baseFeature_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [BaseFeature](BaseFeature.htm).

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |