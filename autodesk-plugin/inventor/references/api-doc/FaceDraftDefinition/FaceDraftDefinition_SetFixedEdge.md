# FaceDraftDefinition.SetFixedEdge Method

Parent Object: [FaceDraftDefinition](../FaceDraftDefinition/FaceDraftDefinition.md)

## Description

Method that set the face draft definition to be kFixedEdgeFaceDraftDefinitionType with input values.

## Syntax

FaceDraftDefinition.**SetFixedEdge**( ***InputFaces*** As [FaceCollection](../FaceCollection/FaceCollection.md), ***FixedEdges*** As [EdgeCollection](../EdgeCollection/EdgeCollection.md), ***PullDirection*** As Object, ***DraftAngle*** As Variant, [***PullDirectionReversed***] As Boolean, [***AbsoluteDraftAngle***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InputFaces | [FaceCollection](../FaceCollection/FaceCollection.md) | Input FaceCollection object that specifies the faces to draft. |
| FixedEdges | [EdgeCollection](../EdgeCollection/EdgeCollection.md) | Input EdgeCollection object that specifies the fixed edges for face draft. |
| PullDirection | Object | Input Object that specifies an object to define the pull direction. This could be a planar Face, an Edge, a WorkPlane or a WorkAxis. |
| DraftAngle | Variant | Input Variant value that specifies the draft angle for face draft. A numeric or string value can be supplied for this property and a parameter will be automatically created after the face draft feature is created. If a numeric value is supplied, the value is in radian, and the parameter is set to the value specified. If a string value is supplied it will be used as the expression for the newly created parameter, if the value is supplied without a unit qualifier it will default to the current document angle unit. The following is a valid entry for it, assuming the parameter d1 already exists and defines a angle “d1+3 deg”. |
| PullDirectionReversed | Boolean | Optioanl input Boolean that specifies whether reverse the pull direction. |
| AbsoluteDraftAngle | Boolean | Optioanl input Boolean that specifies whether the DraftAngle is absolute angle or relative angle against the pull direction. This defaults to True indicating the draft angle is absolute angle value.   This is an optional argument whose default value is True. |

## Version

Introduced in version 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |