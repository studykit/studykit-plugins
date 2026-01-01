# Profile.nativeObject Property

Parent Object: [Profile](Profile.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Profile.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profile\_var" is a variable referencing a Profile object. |

"profile\_var" is a variable referencing a Profile object. ```` ``` #include <Fusion/Sketch/Profile.h>  // Get the value of the property. Ptr<Profile> propertyValue = profile_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [Profile](Profile.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |