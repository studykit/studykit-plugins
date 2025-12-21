# FaceDraftDefinition.SetFixedPlane Method

Parent Object: [FaceDraftDefinition](../FaceDraftDefinition/FaceDraftDefinition.md)

## Description

Method that set the face draft definition to be kFixedPlaneFaceDraftDefinitionType with input values.

## Syntax

FaceDraftDefinition.**SetFixedPlane**( ***InputFaces*** As [FaceCollection](../FaceCollection/FaceCollection.md), ***FixedPlane*** As Object, ***DraftAngle*** As Variant, [***DraftAngleConstraintType***] As [DraftAngleConstraintTypeEnum](../DraftAngleConstraintTypeEnum.md), [***DraftAngleTwo***] As Variant, [***AbsoluteDraftAngle***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InputFaces | [FaceCollection](../FaceCollection/FaceCollection.md) | Input FaceCollection object that specifies the faces to draft. |
| FixedPlane | Object | Input object that specifies the fixed plane for face draft. This can be a planar Face, or a WorkPlane. |
| DraftAngle | Variant | Input Variant value that specifies the draft angle for face draft. A numeric or string value can be supplied for this property and a parameter will be automatically created after the face draft feature is created. If a numeric value is supplied, the value is in radian, and the parameter is set to the value specified. If a string value is supplied it will be used as the expression for the newly created parameter, if the value is supplied without a unit qualifier it will default to the current document angle unit. The following is a valid entry for it, assuming the parameter d1 already exists and defines a angle “d1+3 deg”. |
| DraftAngleConstraintType | [DraftAngleConstraintTypeEnum](../DraftAngleConstraintTypeEnum.md) | Optioanl input DraftAngleConstraintTypeEnum that specifies how the draft angle will be applied to the draft faces on two sides of the fixed plane. Valid inputs are kOneWayDraftAngle ,kSymmetricDraftAngles and kAsymmetricDraftAngles. This defaults to kOneWayDraftAngle. When the kAsymmetricDraftAngles is specified for this argument the DraftAngleTwo is required to specify the draft angle two for the face draft feature. |
| DraftAngleTwo | Variant | Optional input Variant value that specifies the draft angle two for face draft. A numeric or string value can be supplied for this property and a parameter will be automatically created after the face draft feature is created. If a numeric value is supplied, the value is in radian, and the parameter is set to the value specified. If a string value is supplied it will be used as the expression for the newly created parameter, if the value is supplied without a unit qualifier it will default to the current document angle unit. The following is a valid entry for it, assuming the parameter d1 already exists and defines a angle “d1+3 deg”. This is ignored if the DraftAngleConstraintType is not equal to kAsymmetricDraftAngles.   This is an optional argument whose default value is null. |
| AbsoluteDraftAngle | Boolean | Optioanl input Boolean that specifies whether the DraftAngle is absolute angle or relative angle against the pull direction. This defaults to True indicating the draft angle is absolute angle value.   This is an optional argument whose default value is True. |

## Version

Introduced in version 2016
