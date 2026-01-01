# BRepFaces Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepFaces.h>

## Description

BRepFace collection.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BRepFaces_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](BRepFaces_item.htm) | Function that returns the specified face using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](BRepFaces_count.htm) | The number of faces in the collection. |
| [isValid](BRepFaces_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BRepFaces_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[ArrangeFeature.faces](ArrangeFeature_faces.htm), [BaseFeature.faces](BaseFeature_faces.htm), [BossFeature.faces](BossFeature_faces.htm), [BoundaryFillFeature.faces](BoundaryFillFeature_faces.htm), [BoxFeature.faces](BoxFeature_faces.htm), [BRepBody.faces](BRepBody_faces.htm), [BRepEdge.faces](BRepEdge_faces.htm), [BRepFace.tangentiallyConnectedFaces](BRepFace_tangentiallyConnectedFaces.htm), [BRepLump.faces](BRepLump_faces.htm), [BRepShell.faces](BRepShell_faces.htm), [BRepVertex.faces](BRepVertex_faces.htm), [ChamferFeature.faces](ChamferFeature_faces.htm), [CircularPatternFeature.faces](CircularPatternFeature_faces.htm), [CoilFeature.faces](CoilFeature_faces.htm), [CombineFeature.faces](CombineFeature_faces.htm), [CopyPasteBody.faces](CopyPasteBody_faces.htm), [CustomFeature.faces](CustomFeature_faces.htm), [CutPasteBody.faces](CutPasteBody_faces.htm), [CylinderFeature.faces](CylinderFeature_faces.htm), [DeleteFaceFeature.faces](DeleteFaceFeature_faces.htm), [DraftFeature.faces](DraftFeature_faces.htm), [EmbossFeature.faces](EmbossFeature_faces.htm), [ExtendFeature.faces](ExtendFeature_faces.htm), [ExtrudeFeature.endFaces](ExtrudeFeature_endFaces.htm), [ExtrudeFeature.faces](ExtrudeFeature_faces.htm), [ExtrudeFeature.sideFaces](ExtrudeFeature_sideFaces.htm), [ExtrudeFeature.startFaces](ExtrudeFeature_startFaces.htm), [Feature.faces](Feature_faces.htm), [FilletFeature.faces](FilletFeature_faces.htm), [FlangeFeature.faces](FlangeFeature_faces.htm), [FlatPattern.faces](FlatPattern_faces.htm), [FlatPattern.sideFaces](FlatPattern_sideFaces.htm), [FormFeature.faces](FormFeature_faces.htm), [HemFeature.faces](HemFeature_faces.htm), [HoleFeature.endFaces](HoleFeature_endFaces.htm), [HoleFeature.faces](HoleFeature_faces.htm), [HoleFeature.sideFaces](HoleFeature_sideFaces.htm), [LoftFeature.faces](LoftFeature_faces.htm), [LoftFeature.sideFaces](LoftFeature_sideFaces.htm), [MeshCombineFaceGroupsFeature.faces](MeshCombineFaceGroupsFeature_faces.htm), [MeshCombineFeature.faces](MeshCombineFeature_faces.htm), [MeshConvertFeature.faces](MeshConvertFeature_faces.htm), [MeshFeature.faces](MeshFeature_faces.htm), [MeshGenerateFaceGroupsFeature.faces](MeshGenerateFaceGroupsFeature_faces.htm), [MeshReduceFeature.faces](MeshReduceFeature_faces.htm), [MeshRemeshFeature.faces](MeshRemeshFeature_faces.htm), [MeshRepairFeature.faces](MeshRepairFeature_faces.htm), [MeshReverseNormalFeature.faces](MeshReverseNormalFeature_faces.htm), [MeshSeparateFeature.faces](MeshSeparateFeature_faces.htm), [MeshShellFeature.faces](MeshShellFeature_faces.htm), [MeshSmoothFeature.faces](MeshSmoothFeature_faces.htm), [MirrorFeature.faces](MirrorFeature_faces.htm), [MoveFeature.faces](MoveFeature_faces.htm), [OffsetFacesFeature.faces](OffsetFacesFeature_faces.htm), [OffsetFeature.faces](OffsetFeature_faces.htm), [PatchFeature.faces](PatchFeature_faces.htm), [PathPatternFeature.faces](PathPatternFeature_faces.htm), [PipeFeature.endFaces](PipeFeature_endFaces.htm), [PipeFeature.faces](PipeFeature_faces.htm), [PipeFeature.sideFaces](PipeFeature_sideFaces.htm), [PipeFeature.startFaces](PipeFeature_startFaces.htm), [RectangularPatternFeature.faces](RectangularPatternFeature_faces.htm), [RefoldFeature.faces](RefoldFeature_faces.htm), [RemoveFeature.faces](RemoveFeature_faces.htm), [ReplaceFaceFeature.faces](ReplaceFaceFeature_faces.htm), [ReverseNormalFeature.faces](ReverseNormalFeature_faces.htm), [RevolveFeature.endFaces](RevolveFeature_endFaces.htm), [RevolveFeature.faces](RevolveFeature_faces.htm), [RevolveFeature.sideFaces](RevolveFeature_sideFaces.htm), [RevolveFeature.startFaces](RevolveFeature_startFaces.htm), [RibFeature.faces](RibFeature_faces.htm), [RipFeature.faces](RipFeature_faces.htm), [RuledSurfaceFeature.faces](RuledSurfaceFeature_faces.htm), [RuleFilletFeature.faces](RuleFilletFeature_faces.htm), [ScaleFeature.faces](ScaleFeature_faces.htm), [ShellFeature.faces](ShellFeature_faces.htm), [SilhouetteSplitFeature.faces](SilhouetteSplitFeature_faces.htm), [SphereFeature.faces](SphereFeature_faces.htm), [SplitBodyFeature.faces](SplitBodyFeature_faces.htm), [SplitFaceFeature.faces](SplitFaceFeature_faces.htm), [StitchFeature.faces](StitchFeature_faces.htm), [SurfaceDeleteFaceFeature.faces](SurfaceDeleteFaceFeature_faces.htm), [SweepFeature.endFaces](SweepFeature_endFaces.htm), [SweepFeature.faces](SweepFeature_faces.htm), [SweepFeature.sideFaces](SweepFeature_sideFaces.htm), [SweepFeature.startFaces](SweepFeature_startFaces.htm), [TessellateFeature.faces](TessellateFeature_faces.htm), [ThickenFeature.faces](ThickenFeature_faces.htm), [ThreadFeature.faces](ThreadFeature_faces.htm), [TorusFeature.faces](TorusFeature_faces.htm), [TrimFeature.faces](TrimFeature_faces.htm), [UnfoldFeature.faces](UnfoldFeature_faces.htm), [UnstitchFeature.faces](UnstitchFeature_faces.htm), [UntrimFeature.faces](UntrimFeature_faces.htm), [VolumetricCustomFeature.faces](VolumetricCustomFeature_faces.htm), [VolumetricModelToMeshFeature.faces](VolumetricModelToMeshFeature_faces.htm), [WebFeature.faces](WebFeature_faces.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |