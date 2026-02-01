# ShellFeature.nativeObject Property

Parent Object: [ShellFeature](ShellFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeature.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeature\_var" is a variable referencing a ShellFeature object. |

"shellFeature\_var" is a variable referencing a ShellFeature object. ```` ``` #include <Fusion/Features/ShellFeature.h>  // Get the value of the property. Ptr<ShellFeature> propertyValue = shellFeature_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [ShellFeature](ShellFeature.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |