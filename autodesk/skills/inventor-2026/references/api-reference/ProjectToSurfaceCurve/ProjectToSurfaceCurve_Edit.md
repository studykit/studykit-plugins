# ProjectToSurfaceCurve.Edit Method

Parent Object: [ProjectToSurfaceCurve](../ProjectToSurfaceCurve/ProjectToSurfaceCurve.md)

## Description

Method that edits all of the inputs used to compute the project to surface curve. This method is more efficient than setting each of the individual properties since this will result in a single compute rather than computing after each property edit.

## Syntax

ProjectToSurfaceCurve.**Edit**( ***Faces*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***Curves*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***ProjectionType***] As Variant, [***ProjectDirection***] As Variant ) As [ProjectToSurfaceCurve](../ProjectToSurfaceCurve/ProjectToSurfaceCurve.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Faces | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that specifies the faces and/or work planes to project curves to. Valid objects for this argument include Face and WorkPlane. |
| Curves | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that specifies the curves to project. This can be one or more 2D/3D sketch entities, the sketch entities need not to be from the same sketch. |
| ProjectionType | Variant | Optional input ProjectCurveToSufaceTypeEnum that specifies the projection type. If not specified this argument defaults to kProjectAlongVectorType and the PorjectDirection can be specified, and the Curves can include 2D&3D sketch entities. If kProjectToClosestPointType is specified the Curves can include 2D&3D sketch entities. If kWrapToFaceType is specified, the Faces should be developable faces, otherwise an error would occur. The Curves should include 2D sketch entities only. |
| ProjectDirection | Variant | Optional input an object to specify the project direction. The direction is bidirectional. This is ignored if the ProjectionType is not specified as kProjectAlongVectorType. If not specified the normal of the sketch of first selected sketch curve is used. Valid objects are: · Linear Edge/WorkAxis, the direction of the edge is used. · Planar Face/WorkPlane, the normal of the face is used. · Cylindrical/conical/elliptical Face, the axis of the face is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2021
