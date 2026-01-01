# NurbsSurface.getData Method

Parent Object: [NurbsSurface](NurbsSurface.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsSurface.h>

## Description

Gets the data that defines the NURBS surface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nurbsSurface\_var" is a variable referencing a [NurbsSurface](NurbsSurface.htm) object. |

```` ```  #include <Core/Geometry/NurbsSurface.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| degreeU | integer | The output degree in the U direction. |
| degreeV | integer | The output degree in the V direction. |
| controlPointCountU | integer | The output number of control points in the U direction. |
| controlPointCountV | integer | The output number of control points in the V direction. |
| controlPoints | Point3D[] | An output array of surface control points. |
| knotsU | double[] | The output knot vector for the U direction. |
| knotsV | double[] | The output knot vector for the V direction. |
| weights | double[] | An output array of weights that corresponds to the control points of the surface. |
| propertiesU | [NurbsSurfaceProperties](NurbsSurfaceProperties.htm) | The output properties (NurbsSurfaceProperties) of the surface in the U direction. |
| propertiesV | [NurbsSurfaceProperties](NurbsSurfaceProperties.htm) | The output properties (NurbsSurfaceProperties) of the surface in the V direction. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |