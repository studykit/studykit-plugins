# NurbsSurface.surfaceType Property

Parent Object: [NurbsSurface](NurbsSurface.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsSurface.h>

## Description

Returns the surface type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nurbsSurface\_var" is a variable referencing a NurbsSurface object. |

"nurbsSurface\_var" is a variable referencing a NurbsSurface object. ```` ``` #include <Core/Geometry/NurbsSurface.h>  // Get the value of the property. SurfaceTypes propertyValue = nurbsSurface_var->surfaceType(); ``` ```` |

## Property Value

This is a read only property whose value is a [SurfaceTypes](SurfaceTypes.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |