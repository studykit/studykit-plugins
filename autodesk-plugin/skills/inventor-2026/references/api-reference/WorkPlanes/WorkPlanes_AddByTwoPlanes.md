# WorkPlanes.AddByTwoPlanes Method

Parent Object: [WorkPlanes](../WorkPlanes/WorkPlanes.md)

## Description

Creates a new work plane that bisects the two input planes. This method is not currently supported when creating a work plane within an assembly.

## Syntax

WorkPlanes.**AddByTwoPlanes**( ***Plane1*** As Object, ***Plane2*** As Object, [***QuadrantPoint***] As Variant, [***Construction***] As Boolean ) As [WorkPlane](../WorkPlane/WorkPlane.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Plane1 | Object | Input object that represents a plane. This object can be a planar Face, WorkPlane or PlanarSketch object. |
| Plane2 | Object | Input object that represents a plane. This object can be a planar Face, WorkPlane or PlanarSketch object. |
| QuadrantPoint | Variant | Optional input Point to indicate which quadrant the new work plane should be created in. If the two input planes are parallel this argument will be ignored, while the two input planes are intersected then this argument is required to determine which quadrant the new work plane will be created in. |
| Construction | Boolean | Optional input Boolean that specifies whether to create the work plane as a construction plane or not. The default is False, which indicates to create a standard work plane, not a construction work plane. A construction work plane is hidden from the user and is not displayed graphically or listed in the browser.   This is an optional argument whose default value is False. |

## Version

Introduced in version 6
