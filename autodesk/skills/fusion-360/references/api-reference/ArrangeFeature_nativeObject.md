# ArrangeFeature.nativeObject Property

Parent Object: [ArrangeFeature](ArrangeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeFeature.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeFeature\_var" is a variable referencing an ArrangeFeature object. |

"arrangeFeature\_var" is a variable referencing an ArrangeFeature object. ```` ``` #include <Fusion/Arrange/ArrangeFeature.h>  // Get the value of the property. Ptr<ArrangeFeature> propertyValue = arrangeFeature_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is an [ArrangeFeature](ArrangeFeature.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |