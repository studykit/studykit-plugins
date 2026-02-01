# NurbsSurface.propertiesV Property

Parent Object: [NurbsSurface](NurbsSurface.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsSurface.h>

## Description

Gets the properties (NurbsSurfaceProperties) of the surface in the V direction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nurbsSurface\_var" is a variable referencing a NurbsSurface object. |

"nurbsSurface\_var" is a variable referencing a NurbsSurface object. ```` ``` #include <Core/Geometry/NurbsSurface.h>  // Get the value of the property. NurbsSurfaceProperties propertyValue = nurbsSurface_var->propertiesV(); ``` ```` |

## Property Value

This is a read only property whose value is a [NurbsSurfaceProperties](NurbsSurfaceProperties.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |