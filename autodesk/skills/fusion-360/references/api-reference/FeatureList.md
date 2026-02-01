# FeatureList Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FeatureList.h>

## Description

Provides access to a list of features. This is used in the API to return a list of features from an API call.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](FeatureList_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](FeatureList_item.htm) | Returns the specified folder. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](FeatureList_count.htm) | The number of features in this collection. |
| [isValid](FeatureList_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](FeatureList_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[ArrangeFeature.linkedFeatures](ArrangeFeature_linkedFeatures.htm), [BaseFeature.linkedFeatures](BaseFeature_linkedFeatures.htm), [BossFeature.linkedFeatures](BossFeature_linkedFeatures.htm), [BoundaryFillFeature.linkedFeatures](BoundaryFillFeature_linkedFeatures.htm), [BoxFeature.linkedFeatures](BoxFeature_linkedFeatures.htm), [ChamferFeature.linkedFeatures](ChamferFeature_linkedFeatures.htm), [CircularPatternFeature.linkedFeatures](CircularPatternFeature_linkedFeatures.htm), [CoilFeature.linkedFeatures](CoilFeature_linkedFeatures.htm), [CombineFeature.linkedFeatures](CombineFeature_linkedFeatures.htm), [CopyPasteBody.linkedFeatures](CopyPasteBody_linkedFeatures.htm), [CustomFeature.linkedFeatures](CustomFeature_linkedFeatures.htm), [CutPasteBody.linkedFeatures](CutPasteBody_linkedFeatures.htm), [CylinderFeature.linkedFeatures](CylinderFeature_linkedFeatures.htm), [DeleteFaceFeature.linkedFeatures](DeleteFaceFeature_linkedFeatures.htm), [DraftFeature.linkedFeatures](DraftFeature_linkedFeatures.htm), [EmbossFeature.linkedFeatures](EmbossFeature_linkedFeatures.htm), [ExtendFeature.linkedFeatures](ExtendFeature_linkedFeatures.htm), [ExtrudeFeature.linkedFeatures](ExtrudeFeature_linkedFeatures.htm), [Feature.linkedFeatures](Feature_linkedFeatures.htm), [FilletFeature.linkedFeatures](FilletFeature_linkedFeatures.htm), [FlangeFeature.linkedFeatures](FlangeFeature_linkedFeatures.htm), [FlatPattern.linkedFeatures](FlatPattern_linkedFeatures.htm), [FormFeature.linkedFeatures](FormFeature_linkedFeatures.htm), [HemFeature.linkedFeatures](HemFeature_linkedFeatures.htm), [HoleFeature.linkedFeatures](HoleFeature_linkedFeatures.htm), [LoftFeature.linkedFeatures](LoftFeature_linkedFeatures.htm), [MeshCombineFaceGroupsFeature.linkedFeatures](MeshCombineFaceGroupsFeature_linkedFeatures.htm), [MeshCombineFeature.linkedFeatures](MeshCombineFeature_linkedFeatures.htm), [MeshConvertFeature.linkedFeatures](MeshConvertFeature_linkedFeatures.htm), [MeshFeature.linkedFeatures](MeshFeature_linkedFeatures.htm), [MeshGenerateFaceGroupsFeature.linkedFeatures](MeshGenerateFaceGroupsFeature_linkedFeatures.htm), [MeshReduceFeature.linkedFeatures](MeshReduceFeature_linkedFeatures.htm), [MeshRemeshFeature.linkedFeatures](MeshRemeshFeature_linkedFeatures.htm), [MeshRepairFeature.linkedFeatures](MeshRepairFeature_linkedFeatures.htm), [MeshReverseNormalFeature.linkedFeatures](MeshReverseNormalFeature_linkedFeatures.htm), [MeshSeparateFeature.linkedFeatures](MeshSeparateFeature_linkedFeatures.htm), [MeshShellFeature.linkedFeatures](MeshShellFeature_linkedFeatures.htm), [MeshSmoothFeature.linkedFeatures](MeshSmoothFeature_linkedFeatures.htm), [MirrorFeature.linkedFeatures](MirrorFeature_linkedFeatures.htm), [MoveFeature.linkedFeatures](MoveFeature_linkedFeatures.htm), [OffsetFacesFeature.linkedFeatures](OffsetFacesFeature_linkedFeatures.htm), [OffsetFeature.linkedFeatures](OffsetFeature_linkedFeatures.htm), [PatchFeature.linkedFeatures](PatchFeature_linkedFeatures.htm), [PathPatternFeature.linkedFeatures](PathPatternFeature_linkedFeatures.htm), [PipeFeature.linkedFeatures](PipeFeature_linkedFeatures.htm), [RectangularPatternFeature.linkedFeatures](RectangularPatternFeature_linkedFeatures.htm), [RefoldFeature.linkedFeatures](RefoldFeature_linkedFeatures.htm), [RemoveFeature.linkedFeatures](RemoveFeature_linkedFeatures.htm), [ReplaceFaceFeature.linkedFeatures](ReplaceFaceFeature_linkedFeatures.htm), [ReverseNormalFeature.linkedFeatures](ReverseNormalFeature_linkedFeatures.htm), [RevolveFeature.linkedFeatures](RevolveFeature_linkedFeatures.htm), [RibFeature.linkedFeatures](RibFeature_linkedFeatures.htm), [RipFeature.linkedFeatures](RipFeature_linkedFeatures.htm), [RuledSurfaceFeature.linkedFeatures](RuledSurfaceFeature_linkedFeatures.htm), [RuleFilletFeature.linkedFeatures](RuleFilletFeature_linkedFeatures.htm), [ScaleFeature.linkedFeatures](ScaleFeature_linkedFeatures.htm), [ShellFeature.linkedFeatures](ShellFeature_linkedFeatures.htm), [SilhouetteSplitFeature.linkedFeatures](SilhouetteSplitFeature_linkedFeatures.htm), [SphereFeature.linkedFeatures](SphereFeature_linkedFeatures.htm), [SplitBodyFeature.linkedFeatures](SplitBodyFeature_linkedFeatures.htm), [SplitFaceFeature.linkedFeatures](SplitFaceFeature_linkedFeatures.htm), [StitchFeature.linkedFeatures](StitchFeature_linkedFeatures.htm), [SurfaceDeleteFaceFeature.linkedFeatures](SurfaceDeleteFaceFeature_linkedFeatures.htm), [SweepFeature.linkedFeatures](SweepFeature_linkedFeatures.htm), [TessellateFeature.linkedFeatures](TessellateFeature_linkedFeatures.htm), [ThickenFeature.linkedFeatures](ThickenFeature_linkedFeatures.htm), [ThreadFeature.linkedFeatures](ThreadFeature_linkedFeatures.htm), [TorusFeature.linkedFeatures](TorusFeature_linkedFeatures.htm), [TrimFeature.linkedFeatures](TrimFeature_linkedFeatures.htm), [UnfoldFeature.linkedFeatures](UnfoldFeature_linkedFeatures.htm), [UnstitchFeature.linkedFeatures](UnstitchFeature_linkedFeatures.htm), [UntrimFeature.linkedFeatures](UntrimFeature_linkedFeatures.htm), [VolumetricCustomFeature.linkedFeatures](VolumetricCustomFeature_linkedFeatures.htm), [VolumetricModelToMeshFeature.linkedFeatures](VolumetricModelToMeshFeature_linkedFeatures.htm), [WebFeature.linkedFeatures](WebFeature_linkedFeatures.htm)

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |