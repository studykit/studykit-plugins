# PartFeatures Object

## Description

The PartFeatures collection object. Presents the current view of objects and allows their creation.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CreatePath](../PartFeatures/PartFeatures_CreatePath.md) | Method that creates a path used to define the shape of several part features such as sweep, rectangular pattern, split, etc. All other 2D and 3D curves that are connected to the input curve are obtained and used to create a Path object. The new Path is returned. |
| [CreateSpecifiedPath](../PartFeatures/PartFeatures_CreateSpecifiedPath.md) | Method that creates a path used to define the shape of several part features such as sweep, rectangular pattern, split, etc. The new path is returned. This method will fail if the input curves are not connected end-to-end. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AliasFreeformFeatures](../PartFeatures/PartFeatures_AliasFreeformFeatures.md) | Returns the AliasFrreeformFeatures collection object. |
| [Application](../PartFeatures/PartFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BendPartFeatures](../PartFeatures/PartFeatures_BendPartFeatures.md) | Gets the collection object that besides listing out the subset of part features that are BendPartFeatures, allows the creations of BendPartFeatures. |
| [BossFeatures](../PartFeatures/PartFeatures_BossFeatures.md) | Gets the collection object that lists the subset of part features that are BossFeatures. |
| [BoundaryPatchFeatures](../PartFeatures/PartFeatures_BoundaryPatchFeatures.md) | Property that gets the collection object. Besides listing out the subset of part features that are BoundaryPatches, it allows the creation of new BoundaryPatches. |
| [ChamferFeatures](../PartFeatures/PartFeatures_ChamferFeatures.md) | Property that returns the ChamferFeatures collection object. This collection provides access to existing ChamferFeature objects and provides functionality to create new ChamferFeature objects. |
| [CircularPatternFeatures](../PartFeatures/PartFeatures_CircularPatternFeatures.md) | Property that returns the CircularPatternFeatures collection object. This collection provides access to existing CircularPatternFeature objects and provides functionality to create new CircularPatternFeature objects. |
| [ClientFeatures](../PartFeatures/PartFeatures_ClientFeatures.md) | Property returning the client features collection object. |
| [CoilFeatures](../PartFeatures/PartFeatures_CoilFeatures.md) | Property that returns the CoilFeatures collection object. This collection provides access to existing CoilFeature objects and provides functionality to create new CoilFeature objects. |
| [CombineFeatures](../PartFeatures/PartFeatures_CombineFeatures.md) | Property that returns the CombineFeatures collection object. |
| [Count](../PartFeatures/PartFeatures_Count.md) | Property that returns the number of items in the collection. |
| [DecalFeatures](../PartFeatures/PartFeatures_DecalFeatures.md) | Property that returns the DecalFeatures collection object. This collection provides access to existing DecalFeature objects. |
| [DeleteFaceFeatures](../PartFeatures/PartFeatures_DeleteFaceFeatures.md) | Property that returns the DeleteFaceFeatures collection object. This collection provides access to existing DeleteFaceFeature objects. |
| [DirectEditFeatures](../PartFeatures/PartFeatures_DirectEditFeatures.md) | Gets the collection object that besides listing out the subset of part features that are DirectEdit features. |
| [EmbossFeatures](../PartFeatures/PartFeatures_EmbossFeatures.md) | Property that returns the EmbossFeatures collection object. This collection provides access to existing EmbossFeature objects. |
| [ExtendFeatures](../PartFeatures/PartFeatures_ExtendFeatures.md) | Property that returns the ExtendFeatures collection object. This collection provides access to existing ExtendFeature objects and provides functionality to create new ExtendFeature objects. |
| [ExtrudeFeatures](../PartFeatures/PartFeatures_ExtrudeFeatures.md) | Property that returns the collection object. This collection provides access to existing ExtrudeFeature objects and provides functionality to create new ExtrudeFeature objects. |
| [FaceDraftFeatures](../PartFeatures/PartFeatures_FaceDraftFeatures.md) | Property that returns the FaceDraftFeatures collection object. This collection provides access to existing FaceDraftFeature objects. |
| [FilletFeatures](../PartFeatures/PartFeatures_FilletFeatures.md) | Property that returns the FilletFeatures collection object. This collection provides access to existing FilletFeature objects and provides functionality to create new FilletFeature objects. |
| [FinishFeatures](../PartFeatures/PartFeatures_FinishFeatures.md) | Gets the collection object that lists the subset of part features that are FinishFeatures. |
| [FreeformFeatures](../PartFeatures/PartFeatures_FreeformFeatures.md) | Gets the collection object that besides listing out the subset of part features that are Freeform features, allows the creations of new Freeform features. |
| [GrillFeatures](../PartFeatures/PartFeatures_GrillFeatures.md) | Gets the collection object that lists the subset of part features that are GrillFeatures. |
| [HoleFeatures](../PartFeatures/PartFeatures_HoleFeatures.md) | Property that returns the HoleFeatures collection object. This collection provides access to existing HoleFeature objects and provides functionality to create new HoleFeature objects. |
| [iFeatures](../PartFeatures/PartFeatures_iFeatures.md) | Property that returns the iFeatures collection object. |
| [Item](../PartFeatures/PartFeatures_Item.md) | Returns the specified PartFeature object from the collection. It accesses all of the features regardless of their type. If you increment through the features in the collection they are returned in the same order as they appear in the feature browser. |
| [KnitFeatures](../PartFeatures/PartFeatures_KnitFeatures.md) | Property that returns the KnitFeatures collection object. This collection provides access to existing KnitFeature objects. |
| [LipFeatures](../PartFeatures/PartFeatures_LipFeatures.md) | Gets the collection object that lists the subset of part features that are LipFeatures. |
| [LoftFeatures](../PartFeatures/PartFeatures_LoftFeatures.md) | Property that returns the LoftFeatures collection object. This collection provides access to existing LoftFeature objects and provides functionality to create new LoftFeature objects. |
| [MarkFeatures](../PartFeatures/PartFeatures_MarkFeatures.md) | Gets the collection object that lists the subset of part features that are MarkFeatures. |
| [MirrorFeatures](../PartFeatures/PartFeatures_MirrorFeatures.md) | Property that returns the MirrorFeatures collection object. This collection provides access to existing MirrorFeature objects and provides functionality to create new MirrorFeature objects. |
| [MoveFaceFeatures](../PartFeatures/PartFeatures_MoveFaceFeatures.md) | Property that returns the MoveFaceFeatures collection object. |
| [MoveFeatures](../PartFeatures/PartFeatures_MoveFeatures.md) | Gets the collection object that besides listing out the subset of part features that are Moves, allows the creations of new Moves. |
| [NonParametricBaseFeatures](../PartFeatures/PartFeatures_NonParametricBaseFeatures.md) | Property that returns the NonParametericBaseFeatures collection object. This collection provides access to existing NonParametericBaseFeature objects and provides functionality to create new NonParametericBaseFeature objects. |
| [RectangularPatternFeatures](../PartFeatures/PartFeatures_RectangularPatternFeatures.md) | Property that returns the RectangularPatternFeatures collection object. This collection provides access to existing RectangularPatternFeature objects and provides functionality to create new RectangularPatternFeature objects. |
| [ReferenceFeatures](../PartFeatures/PartFeatures_ReferenceFeatures.md) | Property that returns the ReferenceFeatures collection object. |
| [ReplaceFaceFeatures](../PartFeatures/PartFeatures_ReplaceFaceFeatures.md) | Property that returns the ReplaceFaceFeatures collection object. This collection provides access to existing ReplaceFaceFeature objects. |
| [RestFeatures](../PartFeatures/PartFeatures_RestFeatures.md) | Gets the collection object that lists the subset of part features that are RestFeatures. |
| [RevolveFeatures](../PartFeatures/PartFeatures_RevolveFeatures.md) | Property that returns the RevolveFeatures collection object. This collection provides access to existing RevolveFeature objects and provides functionality to create new RevolveFeature objects. |
| [RibFeatures](../PartFeatures/PartFeatures_RibFeatures.md) | Property that returns the RibFeatures collection object. This collection provides access to existing RibFeature objects. |
| [RuledSurfaceFeatures](../PartFeatures/PartFeatures_RuledSurfaceFeatures.md) | Gets the collection object that lists the subset of part features that are RuledSurfaceFeatures. |
| [RuleFilletFeatures](../PartFeatures/PartFeatures_RuleFilletFeatures.md) | Gets the collection object that lists the subset of part features that are RuleFilletFeatures. |
| [SculptFeatures](../PartFeatures/PartFeatures_SculptFeatures.md) | Property that returns the SculptFeatures collection object. This collection provides access to existing SculptFeature objects and provides functionality to create new SculptFeature objects. |
| [ShellFeatures](../PartFeatures/PartFeatures_ShellFeatures.md) | Property that returns the ShellFeatures collection object. This collection provides access to existing ShellFeature objects. |
| [SimplifyFeatures](../PartFeatures/PartFeatures_SimplifyFeatures.md) | Read-only property that returns the SimplifyFeatures collection object. |
| [SketchDrivenPatternFeatures](../PartFeatures/PartFeatures_SketchDrivenPatternFeatures.md) | Gets the collection object that besides listing out the subset of part features that are SketchDrivenPatterns, allows the creations of new SketchDrivenPatterns. |
| [SnapFitFeatures](../PartFeatures/PartFeatures_SnapFitFeatures.md) | Gets the collection object that lists the subset of part features that are SnapFitFeatures. |
| [SplitFeatures](../PartFeatures/PartFeatures_SplitFeatures.md) | Property that returns the SplitFeatures collection object. This collection provides access to existing SplitFeature objects. |
| [SweepFeatures](../PartFeatures/PartFeatures_SweepFeatures.md) | Property that returns the SweepFeatures collection object. This collection provides access to existing SweepFeature objects and provides functionality to create new SweepFeature objects. |
| [ThickenFeatures](../PartFeatures/PartFeatures_ThickenFeatures.md) | Property that returns the ThickenFeatures collection object. This collection provides access to existing ThickenFeature objects. |
| [ThreadFeatures](../PartFeatures/PartFeatures_ThreadFeatures.md) | Property that returns the ThreadFeatures collection object. This collection provides access to existing ThreadFeature objects and provides functionality to create new ThreadFeature objects. |
| [TrimFeatures](../PartFeatures/PartFeatures_TrimFeatures.md) | Property that returns the TrimFeatures collection object. This collection provides access to existing TrimFeature objects and provides functionality to create new TrimFeature objects. |
| [Type](../PartFeatures/PartFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnwrapFeatures](../PartFeatures/PartFeatures_UnwrapFeatures.md) | Gets the collection object that lists the subset of part features that are UnwrapFeatures. |

## Accessed From

[PartComponentDefinition.Features](../PartComponentDefinition/PartComponentDefinition_Features.md), [SheetMetalComponentDefinition.Features](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_Features.md)

## Derived Classes

[SheetMetalFeatures](../SheetMetalFeatures/SheetMetalFeatures.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |
| [Associative body copy](../../sample-programs/NonParametricBaseFeatures_AddByDefinition_Sample.md) | The following sample demonstrates copying bodies (associatively and non-associatively) across parts in an assembly. |
| [Transient surface body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody2_Sample.md) | The following sample demonstrates the creation of a transient surface body consisting of a single rectangular face. The body is created in transient space and then copied over to a part document as a base feature. |
| [Edit thread features](../../sample-programs/ThreadFeatures_CreateStandardThreadInfo_Sample.md) | The following example demonstrates how to edit an existing thread feature. |

## Version

Introduced in version 4
