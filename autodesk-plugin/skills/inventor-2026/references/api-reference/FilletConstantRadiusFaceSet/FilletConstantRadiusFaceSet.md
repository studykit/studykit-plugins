# FilletConstantRadiusFaceSet Object

## Description

The ConstantRadiusFaceSet object provides access to the faces for a constant radius fillet.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FilletConstantRadiusFaceSet/FilletConstantRadiusFaceSet_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BiasPoint](../FilletConstantRadiusFaceSet/FilletConstantRadiusFaceSet_BiasPoint.md) | Optional input Point object that specifies a bias point to help choose between solutions if there are multiple possibilities. |
| [FacesOne](../FilletConstantRadiusFaceSet/FilletConstantRadiusFaceSet_FacesOne.md) | FaceCollection object that contains the first set of faces for the face fillet feature. This can contain more than one face only if the faces are tangentially connected. The Face.TangentiallyConnectedFaces property can be used to get a collection of faces that are tangent to a given face. |
| [FacesOneReverseDirection](../FilletConstantRadiusFaceSet/FilletConstantRadiusFaceSet_FacesOneReverseDirection.md) | Boolean that indicates whether the side of the surface on which the fillet will be created is flipped. This only applies to faces of a surface and is ignored for faces of a solid. |
| [FacesTwo](../FilletConstantRadiusFaceSet/FilletConstantRadiusFaceSet_FacesTwo.md) | FaceCollection object that contains the second set of faces for the face fillet feature. This can contain more than one face only if the faces are tangentially connected. The Face.TangentiallyConnectedFaces property can be used to get a collection of faces that are tangent to a given face. |
| [FacesTwoReverseDirection](../FilletConstantRadiusFaceSet/FilletConstantRadiusFaceSet_FacesTwoReverseDirection.md) | Boolean that indicates whether the side of the surface on which the fillet was created is flipped. This only applies to faces of a surface and is ignored for faces of a solid. |
| [IncludeTangentFaces](../FilletConstantRadiusFaceSet/FilletConstantRadiusFaceSet_IncludeTangentFaces.md) | Boolean that indicates whether faces were tangential to the faces input in the FacesOne and FacesTwo arguments for the fillet creation. |
| [Radius](../FilletConstantRadiusFaceSet/FilletConstantRadiusFaceSet_Radius.md) | Property that returns the parameter that controls the radius of the fillet. This property will return Nothing if the fillet feature has not been created yet. |
| [Type](../FilletConstantRadiusFaceSet/FilletConstantRadiusFaceSet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[FilletDefinition.AddFaceSet](../FilletDefinition/FilletDefinition_AddFaceSet.md), [FilletDefinition.FaceSet](../FilletDefinition/FilletDefinition_FaceSet.md)

## Version

Introduced in version 11
