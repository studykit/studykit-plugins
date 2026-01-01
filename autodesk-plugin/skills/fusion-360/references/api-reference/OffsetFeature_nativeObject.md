# OffsetFeature.nativeObject Property

Parent Object: [OffsetFeature](OffsetFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFeature.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFeature\_var" is a variable referencing an OffsetFeature object. |

"offsetFeature\_var" is a variable referencing an OffsetFeature object. ```` ``` #include <Fusion/Features/OffsetFeature.h>  // Get the value of the property. Ptr<OffsetFeature> propertyValue = offsetFeature_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is an [OffsetFeature](OffsetFeature.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |