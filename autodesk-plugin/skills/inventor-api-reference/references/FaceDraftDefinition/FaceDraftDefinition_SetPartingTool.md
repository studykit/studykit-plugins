# FaceDraftDefinition.SetPartingTool Method

Parent Object: [FaceDraftDefinition](../FaceDraftDefinition/FaceDraftDefinition.md)

## Description

Method that set the face draft definition to be kPartingToolFaceDraftDefinitionType with input values.

## Syntax

FaceDraftDefinition.**SetPartingTool**( ***InputFaces*** As [FaceCollection](../FaceCollection/FaceCollection.md), ***PartingTool*** As Object, ***PullDirection*** As Object, ***DraftAngle*** As Variant, [***CutMaterial***] As Boolean, [***FixedEdges***] As Variant, [***DraftAngleConstraintType***] As [DraftAngleConstraintTypeEnum](../DraftAngleConstraintTypeEnum.md), [***DraftAngleTwo***] As Variant, [***PullDirectionReversed***] As Boolean, [***AbsoluteDraftAngle***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InputFaces | [FaceCollection](../FaceCollection/FaceCollection.md) | Input FaceCollection object that specifies the faces to draft. |
| PartingTool | Object | Input object that specifies the parting tool for face draft. This can be a 2D&3D sketch profile or work plane or work surface. Valid parting tool should be intersecting with the input faces for drafting. |
| PullDirection | Object | Input Object that specifies an object to define the pull direction. This could be a planar Face, an Edge, a WorkPlane or a WorkAxis. |
| DraftAngle | Variant | Input Variant value that specifies the draft angle for face draft. A numeric or string value can be supplied for this property and a parameter will be automatically created after the face draft feature is created. If a numeric value is supplied, the value is in radian, and the parameter is set to the value specified. If a string value is supplied it will be used as the expression for the newly created parameter, if the value is supplied without a unit qualifier it will default to the current document angle unit. The following is a valid entry for it, assuming the parameter d1 already exists and defines a angle “d1+3 deg”. |
| CutMaterial | Boolean | Optioanl input Boolean that specifies whether the draft face feature is to cut material. This defaults to True indicating the draft face feature is to cut material. |
| FixedEdges | Variant | Optioanl input EdgeCollection object that specifies the fixed edges for face draft. This is ignored if the CutMaterial is True.   This is an optional argument whose default value is null. |
| DraftAngleConstraintType | [DraftAngleConstraintTypeEnum](../DraftAngleConstraintTypeEnum.md) | Optioanl input DraftAngleConstraintTypeEnum that specifies how the draft angle will be applied to the draft faces on two sides of the parting tool. When the CutMaterial is True you can specify the kSymmetricDraftAngles and kAsymmetricDraftAngles, and the kSymmetricDraftAngles is default value in this case. While the CutMaterial is False, valid input values are kSideOneMinDraftAngle, kSideTwoMinDraftAngle and kBothSidesMinDraftAngle, and the kSideOneMinDraftAngle is default value in this case.   This is an optional argument whose default value is 108290. |
| DraftAngleTwo | Variant | Optional input Variant value that specifies the draft angle two for face draft. A numeric or string value can be supplied for this property and a parameter will be automatically created after the face draft feature is created. If a numeric value is supplied, the value is in radian, and the parameter is set to the value specified. If a string value is supplied it will be used as the expression for the newly created parameter, if the value is supplied without a unit qualifier it will default to the current document angle unit. The following is a valid entry for it, assuming the parameter d1 already exists and defines a angle “d1+3 deg”.   This is an optional argument whose default value is null. |
| PullDirectionReversed | Boolean | Optioanl input Boolean that specifies whether reverse the pull direction.   This is an optional argument whose default value is False. |
| AbsoluteDraftAngle | Boolean | Optioanl input Boolean that specifies whether the DraftAngle is absolute angle or relative angle against the pull direction. This defaults to True indicating the draft angle is absolute angle value.   This is an optional argument whose default value is True. |

## Version

Introduced in version 2017
