# Profile Object

## Description

The Profile object defines a set of connected curves used as input for a feature. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../Profile/Profile_Delete.md) | Deletes this profile object. |
| [GetReferenceKey](../Profile/Profile_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Profile/Profile_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../Profile/Profile_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Count](../Profile/Profile_Count.md) | Property that returns the number of items in this collection. |
| [Item](../Profile/Profile_Item.md) | Returns the specified ProfilePath object from the collection. |
| [MergeFaces](../Profile/Profile_MergeFaces.md) | Gets and sets the MergeFaces setting. |
| [Parent](../Profile/Profile_Parent.md) | Property that returns the sketch that the profile was derived from. |
| [RegionProperties](../Profile/Profile_RegionProperties.md) | Returns the RegionProperties object. |
| [Type](../Profile/Profile_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Wires](../Profile/Profile_Wires.md) | Property returning the Wires collection object associated with this Profile. |

## Accessed From

[BreakOutOperation.Profile](../BreakOutOperation/BreakOutOperation_Profile.md), [CoilFeature.Profile](../CoilFeature/CoilFeature_Profile.md), [CoilFeatureProxy.Profile](../CoilFeatureProxy/CoilFeatureProxy_Profile.md), [CutDefinition.Profile](../CutDefinition/CutDefinition_Profile.md), [EmbossFeature.Profile](../EmbossFeature/EmbossFeature_Profile.md), [EmbossFeatureProxy.Profile](../EmbossFeatureProxy/EmbossFeatureProxy_Profile.md), [ExtrudeDefinition.Profile](../ExtrudeDefinition/ExtrudeDefinition_Profile.md), [FaceFeatureDefinition.Profile](../FaceFeatureDefinition/FaceFeatureDefinition_Profile.md), [ProfilePath.Parent](../ProfilePath/ProfilePath_Parent.md), [ProfilePathProxy.Parent](../ProfilePathProxy/ProfilePathProxy_Parent.md), [ProfileProxy.NativeObject](../ProfileProxy/ProfileProxy_NativeObject.md), [Profiles.AddForSolid](../Profiles/Profiles_AddForSolid.md), [Profiles.AddForSurface](../Profiles/Profiles_AddForSurface.md), [Profiles.Item](../Profiles/Profiles_Item.md), [RevolveFeature.Profile](../RevolveFeature/RevolveFeature_Profile.md), [RevolveFeatureProxy.Profile](../RevolveFeatureProxy/RevolveFeatureProxy_Profile.md), [SketchFillRegion.Profile](../SketchFillRegion/SketchFillRegion_Profile.md), [SketchHatchRegion.Profile](../SketchHatchRegion/SketchHatchRegion_Profile.md), [SweepDefinition.Profile](../SweepDefinition/SweepDefinition_Profile.md)

## Derived Classes

[ProfileProxy](../ProfileProxy/ProfileProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |
| [Using Inventor's error dialog](../../sample-programs/ErrorManager_Sample.md) | Demonstrates using Inventor's error dialog. |
| [Edit profile of an extrude feature](../../sample-programs/ExtrudeFeature_Profile_Sample.md) | This sample demonstrates editing the profile of an extrude feature. |
| [Create sheet metal face and fold features](../../sample-programs/FoldFeatures_Add_Sample.md) | This sample demonstrates the creation of sheet metal face and fold features. |
| [Hole Feature - Through holes (RegularAndTapped)](../../sample-programs/HoleFeature_Sample.md) | This sample demonstrates the creation of through holes, both regular and tapped. |
| [Create and Edit an Extrude Feature with a pocket](../../sample-programs/PartFeature_SetEndOfPart_Sample.md) | This sample demonstrates how to edit an extrude feature. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Sketch from Face Silhouette](../../sample-programs/PlanarSketch_AddBySilhouette_Sample.md) | This sample creates a cylindrical solid, creates a new sketch plane and creates some new sketch lines from the actual edges and the apparent (silhouette) edges of the cylinder. |
| [Querying a sketch profile to get regions.](../../sample-programs/Profile_RegionProperties_Sample.md) | This sample demonstrates getting region properties from a sketch profile. |
| [Sketch profile control](../../sample-programs/ProfilePath_AddsMaterial_Sample.md) | This sample demonstrates the usage of the Profiles API to control the shape of the profile. The sample creates three concntric circles and creates an extrusion of the region between the inner circles. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |
| [Thread Feature Create](../../sample-programs/ThreadFeature_Sample.md) | This sample demonstrates the creation of a thread feature. It creates a cylinder in a new part document and creates a thread feature on the cylinder. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |