# FilletDefinition.AddFaceSet Method

Parent Object: [FilletDefinition](../FilletDefinition/FilletDefinition.md)

## Description

Method that creates a new constant radius face set used to create a face fillet. The new FilletFaceSet is returned. If a FilletFaceSet already exists in the definition, it is replaced with this new one.

## Syntax

FilletDefinition.**AddFaceSet**( ***FacesOne*** As [FaceCollection](../FaceCollection/FaceCollection.md), ***FacesTwo*** As [FaceCollection](../FaceCollection/FaceCollection.md), ***Radius*** As Variant, [***IncludeTangentFaces***] As Boolean, [***BiasPoint***] As Variant, [***FacesOneReverseDirection***] As Boolean, [***FacesTwoReverseDirection***] As Boolean ) As [FilletConstantRadiusFaceSet](../FilletConstantRadiusFaceSet/FilletConstantRadiusFaceSet.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FacesOne | [FaceCollection](../FaceCollection/FaceCollection.md) | FaceCollection object that contains the first set of faces for the face fillet feature. This can contain more than one face only if the faces are tangentially connected. The Face.TangentiallyConnectedFaces property can be used to get a collection of faces that are tangent to a given face. |
| FacesTwo | [FaceCollection](../FaceCollection/FaceCollection.md) | FaceCollection object that contains the second set of faces for the face fillet feature. This can contain more than one face only if the faces are tangentially connected. The Face.TangentiallyConnectedFaces property can be used to get a collection of faces that are tangent to a given face. |
| Radius | Variant | Defines the radius of the face fillet. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current distance units of the document. |
| IncludeTangentFaces | Boolean | Boolean that specifies whether to include faces that are tangential to the faces input in the FacesOne and FacesTwo arguments for the fillet creation. If not specified, a default of True is used, indicating that the tangential faces will be used in feature creation. |
| BiasPoint | Variant | Optional input Point object that specifies a bias point to help choose between solutions if there are multiple possibilities.   This is an optional argument whose default value is null. |
| FacesOneReverseDirection | Boolean | Optional input Boolean that specifies whether to flip the side of the surface on which the fillet will be created. This argument only applies to faces of a surface and is ignored for faces of a solid. Default value is False.   This is an optional argument whose default value is False. |
| FacesTwoReverseDirection | Boolean | Optional input Boolean that specifies whether to flip the side of the surface on which the fillet will be created. This argument only applies to faces of a surface and is ignored for faces of a solid. Default value is False.   This is an optional argument whose default value is False. |

## Version

Introduced in version 11
