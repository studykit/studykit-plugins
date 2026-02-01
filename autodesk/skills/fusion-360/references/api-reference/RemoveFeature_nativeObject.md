# RemoveFeature.nativeObject Property

Parent Object: [RemoveFeature](RemoveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RemoveFeature.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"removeFeature\_var" is a variable referencing a RemoveFeature object. |

"removeFeature\_var" is a variable referencing a RemoveFeature object. ```` ``` #include <Fusion/Features/RemoveFeature.h>  // Get the value of the property. Ptr<RemoveFeature> propertyValue = removeFeature_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [RemoveFeature](RemoveFeature.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |