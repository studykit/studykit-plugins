# Profiles Object

## Description

Provides access to all of the objects owned by a particular X and supports the methods to create additional Profiles. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddForSolid](../Profiles/Profiles_AddForSolid.md) | Method that creates a profile containing multiple paths for creating solid features. The paths can include sketch curves as well as text boxes. Individual paths in the returned profile may be deleted to obtain the desired profile. |
| [AddForSurface](../Profiles/Profiles_AddForSurface.md) | Method that creates a profile for creating surface features. The resulting profile could be open or closed. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Profiles/Profiles_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../Profiles/Profiles_Count.md) | Property that returns the number of items in this collection. |
| [Item](../Profiles/Profiles_Item.md) | Returns the specified Profile object from the collection. |
| [Type](../Profiles/Profiles_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DrawingSketch.Profiles](../DrawingSketch/DrawingSketch_Profiles.md), [PlanarSketch.Profiles](../PlanarSketch/PlanarSketch_Profiles.md), [PlanarSketchProxy.Profiles](../PlanarSketchProxy/PlanarSketchProxy_Profiles.md), [SketchBlockDefinition.Profiles](../SketchBlockDefinition/SketchBlockDefinition_Profiles.md), [SketchBlockDefinitionProxy.Profiles](../SketchBlockDefinitionProxy/SketchBlockDefinitionProxy_Profiles.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |
| [Using Inventor's error dialog](../../sample-programs/ErrorManager_Sample.md) | Demonstrates using Inventor's error dialog. |
| [Edit profile of an extrude feature](../../sample-programs/ExtrudeFeature_Profile_Sample.md) | This sample demonstrates editing the profile of an extrude feature. |
| [Create sheet metal face and fold features](../../sample-programs/FoldFeatures_Add_Sample.md) | This sample demonstrates the creation of sheet metal face and fold features. |
| [Querying a sketch profile to get regions.](../../sample-programs/Profile_RegionProperties_Sample.md) | This sample demonstrates getting region properties from a sketch profile. |
| [Sketch profile control](../../sample-programs/ProfilePath_AddsMaterial_Sample.md) | This sample demonstrates the usage of the Profiles API to control the shape of the profile. The sample creates three concntric circles and creates an extrusion of the region between the inner circles. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |
| [Thread Feature Create](../../sample-programs/ThreadFeature_Sample.md) | This sample demonstrates the creation of a thread feature. It creates a cylinder in a new part document and creates a thread feature on the cylinder. |

## Version

Introduced in version 5
