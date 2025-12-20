# UnwrapFeatures.CreateDefinitionWithOptions Method

Parent Object: [UnwrapFeatures](../UnwrapFeatures/UnwrapFeatures.md)

## Description

Method that creates the UnwrapDefinition. The object created does not represent a Unwrap feature but instead is a representation of the information that defines a Unwrap feature. You can use this object as input to the UnwrapFeatures.Add method to create the.

## Syntax

UnwrapFeatures.**CreateDefinitionWithOptions**( ***Faces*** As [FaceCollection](../FaceCollection/FaceCollection.md), [***pOrigin***] As Variant, [***Align***] As [UnwrapResultAlignmentEnum](../UnwrapResultAlignmentEnum.md), [***LinearResult***] As Variant, [***RigidResult***] As Variant, [***AutomaticFaceChain***] As Boolean, [***MergeResultBody***] As Boolean, [***MoreOptions***] As Variant ) As [UnwrapDefinition](../UnwrapDefinition/UnwrapDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Faces | [FaceCollection](../FaceCollection/FaceCollection.md) | Input FaceCollection object that specifies the faces to Unwrap. The faces should be from the same body, otherwise an error would occur. |
| pOrigin | Variant | Optional input a Vertex object that specifies the origin. |
| Align | [UnwrapResultAlignmentEnum](../UnwrapResultAlignmentEnum.md) | Optional input UnwrapResultAlignmentEnum that specifies the alignment of the deformed result. This defaults to kOriginAlignment if it is not specified.   This is an optional argument whose default value is 116993. |
| LinearResult | Variant | Optional input EdgeCollection that specifies a set of consecutive edges to become a single colinear segment in the result. The edges should be from the faces in the InputFaces property and only outer edges that enclose the faces are valid.   This is an optional argument whose default value is null. |
| RigidResult | Variant | Optional input EdgeCollection that specifies a set of consecutive planar edges to remain rigid in the result. The edges should be from the faces in the InputFaces property and only outer edges that enclose the faces are valid.   This is an optional argument whose default value is null. |
| AutomaticFaceChain | Boolean | Optional input Boolean that defines if automatic face chaining along tangentially connected faces should be performed. The default value is True.   This is an optional argument whose default value is True. |
| MergeResultBody | Boolean | Optional input Boolean that defines if merge result body or not. The default value is True.   This is an optional argument whose default value is True. |
| MoreOptions | Variant | Optional input NameValueMap that defines more options for the unwrap definition.    Valid options are:   Name = SeamEdges. Value = EdgeCollection that specifies the seam edges.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |