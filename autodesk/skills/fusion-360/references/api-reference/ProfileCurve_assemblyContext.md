# ProfileCurve.assemblyContext Property

Parent Object: [ProfileCurve](ProfileCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ProfileCurve.h>

## Description

Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profileCurve\_var" is a variable referencing a ProfileCurve object. |

"profileCurve\_var" is a variable referencing a ProfileCurve object. ```` ``` #include <Fusion/Sketch/ProfileCurve.h>  // Get the value of the property. Ptr<Occurrence> propertyValue = profileCurve_var->assemblyContext(); ``` ```` |

## Property Value

This is a read only property whose value is an [Occurrence](Occurrence.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |