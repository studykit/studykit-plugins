# ScaleFeature.nativeObject Property

Parent Object: [ScaleFeature](ScaleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ScaleFeature.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scaleFeature\_var" is a variable referencing a ScaleFeature object. |

"scaleFeature\_var" is a variable referencing a ScaleFeature object. ```` ``` #include <Fusion/Features/ScaleFeature.h>  // Get the value of the property. Ptr<ScaleFeature> propertyValue = scaleFeature_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [ScaleFeature](ScaleFeature.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |