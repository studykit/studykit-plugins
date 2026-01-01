# ReplaceFaceFeature.nativeObject Property

Parent Object: [ReplaceFaceFeature](ReplaceFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReplaceFaceFeature.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"replaceFaceFeature\_var" is a variable referencing a ReplaceFaceFeature object. |

"replaceFaceFeature\_var" is a variable referencing a ReplaceFaceFeature object. ```` ``` #include <Fusion/Features/ReplaceFaceFeature.h>  // Get the value of the property. Ptr<ReplaceFaceFeature> propertyValue = replaceFaceFeature_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [ReplaceFaceFeature](ReplaceFaceFeature.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |