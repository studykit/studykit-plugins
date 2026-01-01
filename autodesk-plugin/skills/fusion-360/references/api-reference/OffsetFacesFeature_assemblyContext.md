# OffsetFacesFeature.assemblyContext Property

Parent Object: [OffsetFacesFeature](OffsetFacesFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFacesFeature.h>

## Description

Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFacesFeature\_var" is a variable referencing an OffsetFacesFeature object. |

"offsetFacesFeature\_var" is a variable referencing an OffsetFacesFeature object. ```` ``` #include <Fusion/Features/OffsetFacesFeature.h>  // Get the value of the property. Ptr<Occurrence> propertyValue = offsetFacesFeature_var->assemblyContext(); ``` ```` |

## Property Value

This is a read only property whose value is an [Occurrence](Occurrence.htm).

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |