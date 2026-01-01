# Decal.nativeObject Property

Parent Object: [Decal](Decal.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Decal.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"decal\_var" is a variable referencing a Decal object. |

"decal\_var" is a variable referencing a Decal object. ```` ``` #include <Fusion/Image/Decal.h>  // Get the value of the property. Ptr<Decal> propertyValue = decal_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [Decal](Decal.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |