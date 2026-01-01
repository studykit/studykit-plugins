# ConstructionPoint.nativeObject Property

Parent Object: [ConstructionPoint](ConstructionPoint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPoint.h>

## Description

The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPoint\_var" is a variable referencing a ConstructionPoint object. |

"constructionPoint\_var" is a variable referencing a ConstructionPoint object. ```` ``` #include <Fusion/Construction/ConstructionPoint.h>  // Get the value of the property. Ptr<ConstructionPoint> propertyValue = constructionPoint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConstructionPoint](ConstructionPoint.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| Â© Copyright 2025 Autodesk, Inc. | Comment on this page. |