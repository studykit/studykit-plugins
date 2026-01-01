# FilletDefinition.AddFullRoundSet Method

Parent Object: [FilletDefinition](../FilletDefinition/FilletDefinition.md)

## Description

Method that creates a new full round set used to create a full round fillet. The new FilletFullRoundSet is returned. If a FilletFullRoundSet already exists in the definition, it is replaced with this new one.

## Syntax

FilletDefinition.**AddFullRoundSet**( ***SideFacesOne*** As [FaceCollection](../FaceCollection/FaceCollection.md), ***CenterFaces*** As [FaceCollection](../FaceCollection/FaceCollection.md), ***SideFacesTwo*** As [FaceCollection](../FaceCollection/FaceCollection.md), [***IncludeTangentFaces***] As Boolean ) As [FilletFullRoundSet](../FilletFullRoundSet/FilletFullRoundSet.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SideFacesOne | [FaceCollection](../FaceCollection/FaceCollection.md) | FaceCollection object that contains the first set of side faces for the full round fillet feature. This can contain more than one face only if the faces are tangentially connected. The Face.TangentiallyConnectedFaces property can be used to get a collection of faces that are tangent to a given face. |
| CenterFaces | [FaceCollection](../FaceCollection/FaceCollection.md) | FaceCollection object that contains the center faces for the full round fillet feature. This can contain more than one face only if the faces are tangentially connected. The Face.TangentiallyConnectedFaces property can be used to get a collection of faces that are tangent to a given face. |
| SideFacesTwo | [FaceCollection](../FaceCollection/FaceCollection.md) | FaceCollection object that contains the second set of side faces for the full round fillet feature. This can contain more than one face only if the faces are tangentially connected. The Face.TangentiallyConnectedFaces property can be used to get a collection of faces that are tangent to a given face. |
| IncludeTangentFaces | Boolean | Optional input Boolean that specifies whether to include faces that are tangential to the faces input in the SideFacesOne, CenterFaces and SideFacesTwo arguments for the fillet creation. If not specified, a default of True is used, indicating that the tangential faces will be used in feature creation. |

## Version

Introduced in version 11
