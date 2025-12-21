# WorkPlaneProxy.SetByLineAndTangent Method

Parent Object: [WorkPlaneProxy](../WorkPlaneProxy/WorkPlaneProxy.md)

## Description

Method that redefines the work plane to be through the input line and tangent to the input surface.

## Syntax

WorkPlaneProxy.**SetByLineAndTangent**( ***Line*** As Object, ***Face*** As [Face](../Face/Face.md), ***ProximityPoint*** As [Point](../Point/Point.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Line | Object | Input object that represents a line. This object can be a linear Edge, WorkAxis, SketchLine, or SketchLine3D object. |
| Face | [Face](../Face/Face.md) | Input Face object that indicates the tangent surface. Valid geometry for the face includes cylinders, cones, and spheres. This face must either be a cylinder whose axis is parallel to the line, a cone that is positioned such that a valid tangent exists, or a sphere. |
| ProximityPoint | [Point](../Point/Point.md) | Input Point object that indicates which of the possible two solutions to use. For cylinders and spheres the plane can be on either side of the surface. Which solution to use will be determined by which side the proximity point is closest to. This point is only used for the initial computation. During a recompute of the model the plane will remain on the same side of the tangent surface regardless of its position relative to the originally specified point. |

## Version

Introduced in version 2008
