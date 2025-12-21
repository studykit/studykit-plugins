# FaceCollection Object

Derived from: [ObjectCollection](../ObjectCollection/ObjectCollection.md) Object

## Description

The FaceCollection object is a transient object created by the CreateFaceCollection method of the TransientObjects object. Typically used when creating a ShellFeature, FaceDraftFeature, etc.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../FaceCollection/FaceCollection_Add.md) | Adds an object to the generic collection. |
| [Clear](../FaceCollection/FaceCollection_Clear.md) | Removes all objects from the generic collection. |
| [Remove](../FaceCollection/FaceCollection_Remove.md) | Method that removes the specified object from the generic collection. |
| [RemoveByObject](../FaceCollection/FaceCollection_RemoveByObject.md) | Method that removes the specified object from the generic object collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [CollectionType](../FaceCollection/FaceCollection_CollectionType.md) | Property returning a constant indicating the Face Collection type. |
| [Count](../FaceCollection/FaceCollection_Count.md) | Property that returns the number of items in this collection. |
| [Item](../FaceCollection/FaceCollection_Item.md) | Allows integer-indexed access to items in the collection. |
| [Type](../FaceCollection/FaceCollection_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyJointDefinition.OriginOneReferencedFaces](../AssemblyJointDefinition/AssemblyJointDefinition_OriginOneReferencedFaces.md), [AssemblyJointDefinition.OriginTwoReferencedFaces](../AssemblyJointDefinition/AssemblyJointDefinition_OriginTwoReferencedFaces.md), [Face.TangentiallyConnectedFaces](../Face/Face_TangentiallyConnectedFaces.md), [FaceDraftDefinition.InputFaces](../FaceDraftDefinition/FaceDraftDefinition_InputFaces.md), [FaceProxy.TangentiallyConnectedFaces](../FaceProxy/FaceProxy_TangentiallyConnectedFaces.md), [FilletConstantRadiusFaceSet.FacesOne](../FilletConstantRadiusFaceSet/FilletConstantRadiusFaceSet_FacesOne.md), [FilletConstantRadiusFaceSet.FacesTwo](../FilletConstantRadiusFaceSet/FilletConstantRadiusFaceSet_FacesTwo.md), [FilletFullRoundSet.CenterFaces](../FilletFullRoundSet/FilletFullRoundSet_CenterFaces.md), [FilletFullRoundSet.SideFacesOne](../FilletFullRoundSet/FilletFullRoundSet_SideFacesOne.md), [FilletFullRoundSet.SideFacesTwo](../FilletFullRoundSet/FilletFullRoundSet_SideFacesTwo.md), [ModelSurfaceTextureSymbolDefinition.Faces](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_Faces.md), [ModelToleranceFeature.AllFaces](../ModelToleranceFeature/ModelToleranceFeature_AllFaces.md), [ModelToleranceFeatureDefinition.Faces](ModelToleranceFeatureDefinition_Faces.md), [ModelToleranceFeatureProxy.AllFaces](../ModelToleranceFeatureProxy/ModelToleranceFeatureProxy_AllFaces.md), [MoveFaceDefinition.Faces](../MoveFaceDefinition/MoveFaceDefinition_Faces.md), [ReplaceFaceDefinition.ExistingFaces](../ReplaceFaceDefinition/ReplaceFaceDefinition_ExistingFaces.md), [ShellDefinition.InputFaces](../ShellDefinition/ShellDefinition_InputFaces.md), [ShellThicknessFaceSet.Faces](../ShellThicknessFaceSet/ShellThicknessFaceSet_Faces.md), [SilhouetteCurve.ExcludedFaces](../SilhouetteCurve/SilhouetteCurve_ExcludedFaces.md), [SilhouetteCurveProxy.ExcludedFaces](../SilhouetteCurveProxy/SilhouetteCurveProxy_ExcludedFaces.md), [SketchDrivenPatternDefinition.ReferenceFaces](../SketchDrivenPatternDefinition/SketchDrivenPatternDefinition_ReferenceFaces.md), [TransientObjects.CreateFaceCollection](../TransientObjects/TransientObjects_CreateFaceCollection.md), [UnwrapDefinition.InputFaces](../UnwrapDefinition/UnwrapDefinition_InputFaces.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [Finish Feature Creation](../../sample-programs/FinishFeatureCreation_Sample.md) | This sample demonstrates how to create a finish feature. |

## Version

Introduced in version 9
