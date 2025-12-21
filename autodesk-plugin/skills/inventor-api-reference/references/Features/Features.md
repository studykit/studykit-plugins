# Features Object

## Description

Represents the collection of features in the assembly context. The API does not yet support addition of assembly features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CreatePath](../Features/Features_CreatePath.md) | Method that creates a path used to define the shape of several part features such as Sweep, RectangularPattern, Split, etc. All other 2D and 3D curves that are connected to the input curve are obtained and used to create a Path object. The new Path is returned. |
| [CreateSpecifiedPath](../Features/Features_CreateSpecifiedPath.md) | Method that creates a path used to define the shape of several part features such as Sweep, RectangularPattern, Split, etc. The new Path is returned. This method will fail if the input curves are not connected end to end. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Features/Features_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ChamferFeatures](../Features/Features_ChamferFeatures.md) | Property that returns the ChamferFeatures collection object. This collection provides access to existing ChamferFeature objects. |
| [CircularPatternFeatures](../Features/Features_CircularPatternFeatures.md) | Property that returns the CircularPatternFeatures collection object. This collection provides access to existing CircularPatternFeature objects. |
| [ClientFeatures](../Features/Features_ClientFeatures.md) | Gets the Client Features collection object. |
| [Count](../Features/Features_Count.md) |  |
| [ExtrudeFeatures](../Features/Features_ExtrudeFeatures.md) | Property that returns the collection object. This collection provides access to existing ExtrudeFeature objects. |
| [FilletFeatures](../Features/Features_FilletFeatures.md) | Property that returns the FilletFeatures collection object. This collection provides access to existing FilletFeature objects. |
| [FinishFeatures](../Features/Features_FinishFeatures.md) | Gets the collection object that besides listing out the subset of features that are FinishFeatures. |
| [HoleFeatures](../Features/Features_HoleFeatures.md) | Property that returns the HoleFeatures collection object. This collection provides access to existing HoleFeature objects. |
| [Item](../Features/Features_Item.md) | Returns the specified feature from the collection. |
| [MirrorFeatures](../Features/Features_MirrorFeatures.md) | Property that returns the MirrorFeatures collection object. This collection provides access to existing MirrorFeature objects. |
| [MoveFaceFeatures](../Features/Features_MoveFaceFeatures.md) | Property that returns the MoveFaceFeatures collection object. This collection provides access to existing MoveFaceFeatures objects. |
| [RectangularPatternFeatures](../Features/Features_RectangularPatternFeatures.md) | Property that returns the RectangularPatternFeatures collection object. This collection provides access to existing RectangularPatternFeature objects. |
| [RevolveFeatures](../Features/Features_RevolveFeatures.md) | Property that returns the RevolveFeatures collection object. This collection provides access to existing RevolveFeature objects. |
| [SketchDrivenPatternFeatures](../Features/Features_SketchDrivenPatternFeatures.md) | Gets the collection object that besides listing out the subset of features that are SketchDrivenPatterns, allows the creations of new SketchDrivenPatterns. |
| [SweepFeatures](../Features/Features_SweepFeatures.md) | Property that returns the SweepFeatures collection object. This collection provides access to existing SweepFeature objects. |
| [ThreadFeatures](../Features/Features_ThreadFeatures.md) | Gets the collection object that besides listing out the subset of features that are Threads, allows the creations of new Threads. |
| [Type](../Features/Features_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyComponentDefinition.Features](../AssemblyComponentDefinition/AssemblyComponentDefinition_Features.md), [WeldmentComponentDefinition.Features](../WeldmentComponentDefinition/WeldmentComponentDefinition_Features.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |
| [Create sheet metal lofted flange feature](../../sample-programs/LoftedFlangeFeatures_Add_Sample.md) | The following sample demonstrates the creation of a sheet metal lofted flange feature. |
| [Part SimplifyFeature Sample](../../sample-programs/PartSimplifyFeatureSample_Sample.md) | This sample demonstrates how to create a simplify feature in part document. |

## Version

Introduced in version 10
