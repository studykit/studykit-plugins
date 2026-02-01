# BRepBodies Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBodies.h>

## Description

The BRepBodies collection provides access to all of the B-Rep bodies within a component.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](BRepBodies_add.htm) | Creates a new BRepBody object. The input can be a persisted or transient BRepBody and the result is a persisted BRepBody. In a direct modeling design, the BRepBody is created within the component the BRepBodies collection was obtained from. In a parametric modeling design, the new BRepBody is created within the specified Base Feature. |
| [classType](BRepBodies_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](BRepBodies_item.htm) | Function that returns the specified body using an index into the collection. |
| [itemByName](BRepBodies_itemByName.htm) | Returns a specific body using the name of the body within the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](BRepBodies_count.htm) | Returns the number of bodies in the collection. |
| [isValid](BRepBodies_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BRepBodies_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[ArrangeFeature.bodies](ArrangeFeature_bodies.htm), [BaseComponent.bRepBodies](BaseComponent_bRepBodies.htm), [BaseFeature.bodies](BaseFeature_bodies.htm), [BossFeature.bodies](BossFeature_bodies.htm), [BoundaryFillFeature.bodies](BoundaryFillFeature_bodies.htm), [BoxFeature.bodies](BoxFeature_bodies.htm), [ChamferFeature.bodies](ChamferFeature_bodies.htm), [CircularPatternFeature.bodies](CircularPatternFeature_bodies.htm), [CoilFeature.bodies](CoilFeature_bodies.htm), [CombineFeature.bodies](CombineFeature_bodies.htm), [Component.bRepBodies](Component_bRepBodies.htm), [CopyPasteBody.bodies](CopyPasteBody_bodies.htm), [CustomFeature.bodies](CustomFeature_bodies.htm), [CutPasteBody.bodies](CutPasteBody_bodies.htm), [CylinderFeature.bodies](CylinderFeature_bodies.htm), [DeleteFaceFeature.bodies](DeleteFaceFeature_bodies.htm), [DraftFeature.bodies](DraftFeature_bodies.htm), [EmbossFeature.bodies](EmbossFeature_bodies.htm), [ExtendFeature.bodies](ExtendFeature_bodies.htm), [ExtrudeFeature.bodies](ExtrudeFeature_bodies.htm), [Feature.bodies](Feature_bodies.htm), [FilletFeature.bodies](FilletFeature_bodies.htm), [FlangeFeature.bodies](FlangeFeature_bodies.htm), [FlatPattern.bodies](FlatPattern_bodies.htm), [FlatPatternComponent.bRepBodies](FlatPatternComponent_bRepBodies.htm), [FormFeature.bodies](FormFeature_bodies.htm), [HemFeature.bodies](HemFeature_bodies.htm), [HoleFeature.bodies](HoleFeature_bodies.htm), [LoftFeature.bodies](LoftFeature_bodies.htm), [MeshCombineFaceGroupsFeature.bodies](MeshCombineFaceGroupsFeature_bodies.htm), [MeshCombineFeature.bodies](MeshCombineFeature_bodies.htm), [MeshConvertFeature.bodies](MeshConvertFeature_bodies.htm), [MeshFeature.bodies](MeshFeature_bodies.htm), [MeshGenerateFaceGroupsFeature.bodies](MeshGenerateFaceGroupsFeature_bodies.htm), [MeshReduceFeature.bodies](MeshReduceFeature_bodies.htm), [MeshRemeshFeature.bodies](MeshRemeshFeature_bodies.htm), [MeshRepairFeature.bodies](MeshRepairFeature_bodies.htm), [MeshReverseNormalFeature.bodies](MeshReverseNormalFeature_bodies.htm), [MeshSeparateFeature.bodies](MeshSeparateFeature_bodies.htm), [MeshShellFeature.bodies](MeshShellFeature_bodies.htm), [MeshSmoothFeature.bodies](MeshSmoothFeature_bodies.htm), [MirrorFeature.bodies](MirrorFeature_bodies.htm), [MoveFeature.bodies](MoveFeature_bodies.htm), [Occurrence.bRepBodies](Occurrence_bRepBodies.htm), [OffsetFacesFeature.bodies](OffsetFacesFeature_bodies.htm), [OffsetFeature.bodies](OffsetFeature_bodies.htm), [PatchFeature.bodies](PatchFeature_bodies.htm), [PathPatternFeature.bodies](PathPatternFeature_bodies.htm), [PipeFeature.bodies](PipeFeature_bodies.htm), [RectangularPatternFeature.bodies](RectangularPatternFeature_bodies.htm), [RefoldFeature.bodies](RefoldFeature_bodies.htm), [RemoveFeature.bodies](RemoveFeature_bodies.htm), [ReplaceFaceFeature.bodies](ReplaceFaceFeature_bodies.htm), [ReverseNormalFeature.bodies](ReverseNormalFeature_bodies.htm), [RevolveFeature.bodies](RevolveFeature_bodies.htm), [RibFeature.bodies](RibFeature_bodies.htm), [RipFeature.bodies](RipFeature_bodies.htm), [RuledSurfaceFeature.bodies](RuledSurfaceFeature_bodies.htm), [RuleFilletFeature.bodies](RuleFilletFeature_bodies.htm), [ScaleFeature.bodies](ScaleFeature_bodies.htm), [ShellFeature.bodies](ShellFeature_bodies.htm), [SilhouetteSplitFeature.bodies](SilhouetteSplitFeature_bodies.htm), [SphereFeature.bodies](SphereFeature_bodies.htm), [SplitBodyFeature.bodies](SplitBodyFeature_bodies.htm), [SplitFaceFeature.bodies](SplitFaceFeature_bodies.htm), [StitchFeature.bodies](StitchFeature_bodies.htm), [SurfaceDeleteFaceFeature.bodies](SurfaceDeleteFaceFeature_bodies.htm), [SweepFeature.bodies](SweepFeature_bodies.htm), [TemporaryBRepManager.createFromFile](TemporaryBRepManager_createFromFile.htm), [TessellateFeature.bodies](TessellateFeature_bodies.htm), [ThickenFeature.bodies](ThickenFeature_bodies.htm), [ThreadFeature.bodies](ThreadFeature_bodies.htm), [TorusFeature.bodies](TorusFeature_bodies.htm), [TrimFeature.bodies](TrimFeature_bodies.htm), [UnfoldFeature.bodies](UnfoldFeature_bodies.htm), [UnstitchFeature.bodies](UnstitchFeature_bodies.htm), [UntrimFeature.bodies](UntrimFeature_bodies.htm), [VolumetricCustomFeature.bodies](VolumetricCustomFeature_bodies.htm), [VolumetricModelToMeshFeature.bodies](VolumetricModelToMeshFeature_bodies.htm), [WebFeature.bodies](WebFeature_bodies.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Get Volume of Active Design API Sample](GetsVolumeOfActiveDesign_Sample.htm) | Traverses through the active design and totals the volume of every body within the design. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |