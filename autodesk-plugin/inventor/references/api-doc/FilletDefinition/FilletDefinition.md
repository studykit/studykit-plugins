# FilletDefinition Object

## Description

The FilletDefinition object is used to define all of the input required for fillet features. It is also used to query and edit existing fillet features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddConstantRadiusEdgeSet](../FilletDefinition/FilletDefinition_AddConstantRadiusEdgeSet.md) | Method that creates a new constant radius edge set. The new FilletDefinition is returned. |
| [AddFaceSet](../FilletDefinition/FilletDefinition_AddFaceSet.md) | Method that creates a new constant radius face set used to create a face fillet. The new FilletFaceSet is returned. If a FilletFaceSet already exists in the definition, it is replaced with this new one. |
| [AddFullRoundSet](../FilletDefinition/FilletDefinition_AddFullRoundSet.md) | Method that creates a new full round set used to create a full round fillet. The new FilletFullRoundSet is returned. If a FilletFullRoundSet already exists in the definition, it is replaced with this new one. |
| [AddVariableRadiusEdgeSet](../FilletDefinition/FilletDefinition_AddVariableRadiusEdgeSet.md) | Method that creates a new variable radius edge set. Intermediate radii can be defined using the AddIntermediatePoint method of the FilletVariableRadiusEdgeSet object returned by this method. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FilletDefinition/FilletDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [EdgeSetCount](../FilletDefinition/FilletDefinition_EdgeSetCount.md) | Property that specifies the number of edge sets currently defined in the definition. This property always returns 0 if the FilletType is not kEdgeFillet. |
| [EdgeSetItem](../FilletDefinition/FilletDefinition_EdgeSetItem.md) | Method that returns the specified FilletRadiusEdgeSet object from the collection. This will return either a FilletConstantRadiusEdgeSet or FilletVariableRadiusEdgeSet object. |
| [FaceSet](../FilletDefinition/FilletDefinition_FaceSet.md) | Property that returns the FilletConstantRadiusFaceSet object that defines the inputs used to create a face fillet. This property returns Nothing if the FilletType is not kFaceFillet. |
| [FilletType](../FilletDefinition/FilletDefinition_FilletType.md) | Property that returns the type of the fillet. Possible return values are kEdgeFillet, kFaceFillet and kFullRoundFillet. |
| [FullRoundSet](../FilletDefinition/FilletDefinition_FullRoundSet.md) | property that returns the FilletFullRoundSet object that defines the inputs used to create a full round fillet. This property returns Nothing if the FilletType is not kFullRoundFillet. |
| [Parent](../FilletDefinition/FilletDefinition_Parent.md) | Property that returns the parent FilletFeature of the definition. |
| [SetbackVertexCount](../FilletDefinition/FilletDefinition_SetbackVertexCount.md) | Property that specifies the number of possible vertex setbacks available for the current set of edges in the definition. This property always returns 0 if the FilletType is not kEdgeFillet. |
| [SetbackVertexItem](../FilletDefinition/FilletDefinition_SetbackVertexItem.md) | Returns the specified FilletSetbackVertex object from the definition. |
| [Type](../FilletDefinition/FilletDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[FilletFeature.FilletDefinition](../FilletFeature/FilletFeature_FilletDefinition.md), [FilletFeatureProxy.FilletDefinition](../FilletFeatureProxy/FilletFeatureProxy_FilletDefinition.md), [FilletFeatures.CreateFilletDefinition](../FilletFeatures/FilletFeatures_CreateFilletDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Fillet Feature (Complex)](../../sample-programs/FilletFeature2_Sample.md) | This sample demonstrates creating a complex fillet. The result in this case has several different constant radii fillets and two edges that use variable radius, with one of these having a different radius defined along the edge. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |