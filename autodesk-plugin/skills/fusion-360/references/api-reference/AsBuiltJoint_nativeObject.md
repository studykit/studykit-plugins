# AsBuiltJoint.nativeObject Property

Parent Object: [AsBuiltJoint](AsBuiltJoint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJoint.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"asBuiltJoint\_var" is a variable referencing an AsBuiltJoint object. |

"asBuiltJoint\_var" is a variable referencing an AsBuiltJoint object. ```` ``` #include <Fusion/Components/AsBuiltJoint.h>  // Get the value of the property. Ptr<AsBuiltJoint> propertyValue = asBuiltJoint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is an [AsBuiltJoint](AsBuiltJoint.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |