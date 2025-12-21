# WorkPlaneProxy.SetByTwoPlanes Method

Parent Object: [WorkPlaneProxy](../WorkPlaneProxy/WorkPlaneProxy.md)

## Description

Method that redefines a bisection work plane to be based on the two planes.

## Syntax

WorkPlaneProxy.**SetByTwoPlanes**( ***Plane1*** As Object, ***Plane2*** As Object, [***QuadrantPoint***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Plane1 | Object | Input object that represents a plane. This object can be a planar Face, WorkPlane or PlanarSketch object. |
| Plane2 | Object | Input object that represents a plane. This object can be a planar Face, WorkPlane or PlanarSketch object. |
| QuadrantPoint | Variant | Optional input Point to indicate which quadrant the new work plane should be created in. If the two input planes are parallel this argument will be ignored, while the two input planes are intersected then this argument is required to determine which quadrant the new work plane will be created in. |

## Version

Introduced in version 2008
