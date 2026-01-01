# UnstitchFeature.nativeObject Property

Parent Object: [UnstitchFeature](UnstitchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UnstitchFeature.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unstitchFeature\_var" is a variable referencing a UnstitchFeature object. |

"unstitchFeature\_var" is a variable referencing a UnstitchFeature object. ```` ``` #include <Fusion/Features/UnstitchFeature.h>  // Get the value of the property. Ptr<UnstitchFeature> propertyValue = unstitchFeature_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [UnstitchFeature](UnstitchFeature.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |