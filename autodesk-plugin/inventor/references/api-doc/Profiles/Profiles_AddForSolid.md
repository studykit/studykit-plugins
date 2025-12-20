# Profiles.AddForSolid Method

Parent Object: [Profiles](../Profiles/Profiles.md)

## Description

Method that creates a profile containing multiple paths for creating solid features. The paths can include sketch curves as well as text boxes. Individual paths in the returned profile may be deleted to obtain the desired profile.

## Remarks

If sketch curves are included in the profile, the topological information defined by the intersection and connection of sketch entities with one another is used to define the various profile paths. A profile path consists of one or more profile entities. If a profile path contains only one profile entity, then it implies that a single sketch curve (e.g. a sketch circle) defines the profile path. If the profile path comprises of multiple profile entities, then a set of connected sketch curves defines the profile path with each profile entity representing an entire sketch curve or a portion of it. If text boxes are included in the profile, then each text box will be associated with a single profile path. Since a single instance of a text box that contains some text essentially consists of a group of one or more characters which have a certain thickness, the outline of each character in the text can be considered to form a closed loop. All the characters in a given text box will be treated as a single entity and grouped to form a single profile path. The profile paths defined by the sketch curves will be independently determined from the profile paths defined by the text boxes. The sketch curves will be evaluated based on their topological information to define a set of profile paths that comprises of only the sketch curves. The text boxes will be used to define a different set of profile paths such that each text box will correspond to a unique profile path. Therefore, a given profile path will either include sketch curves or a single text box but not both.

## Syntax

Profiles.**AddForSolid**( [***Combine***] As Boolean, [***ProfilePathSegments***] As Variant, [***Reserved***] As Variant ) As [Profile](../Profile/Profile.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Combine | Boolean | Optional input Boolean that specifies whether to combine the profile paths obtained when this method is used to create a new profile. For instance, let us take the example of a sketch containing two concentric circles. If this argument is specified to be true, the resulting profile will contain 2 profile paths, and the profile path corresponding to the inner circle will have its AddsMaterial flag set to False. Hence, the resulting profile is a circular disc with a circular cut\-out. If the Combine flag is specified to be False, the resulting profile will contain 2 profile paths with the AddsMaterial flag set to True for both paths. If the sketch contains text boxes, then the profile paths corresponding to them will always have the AddsMaterial flag set to True irrespective of whether the Combine flag is specified to be True or False. |
| ProfilePathSegments | Variant | Optional input ObjectCollection that can contain sketch curves as well as text boxes. If sketch curves are specified, then the profile created by this method will include profile paths that are comprised of the exact set of sketch curves specified in the ObjectCollection. If text boxes are specified, then the profile created by this method will include profile paths that correspond to the exact set of text boxes specified in the ObjectCollection. Each text box in the collection will correspond to a unique profile path. If not specified, all the possible profile paths including sketch curves as well as text boxes will be included. This argument is ignored if the Combine argument is specified to be True.     This is an optional argument whose default value is null. |
| Reserved | Variant | Optional input Variant reserved for future use. This argument is currently ignored.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |
| [Sketch fill region](../../sample-programs/DrawingSketch_SketchFillRegions_Sample.md) | This sample demonstrates the sketch fill functionality in drawing sketches. |
| [Using Inventor's error dialog](../../sample-programs/ErrorManager_Sample.md) | Demonstrates using Inventor's error dialog. |
| [Extrude Feature - Create Block with Pocket](../../sample-programs/ExtrudeFeature_Sample.md) | This sample demonstrates creating a simple solid consisting a block with a pocket. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Edit profile of an extrude feature](../../sample-programs/ExtrudeFeature_Profile_Sample.md) | This sample demonstrates editing the profile of an extrude feature. |
| [Extrude sketch text](../../sample-programs/ExtrudeFeatures_AddByDistanceExtent_Sample.md) | This sample demonstrates the creation of an extrude feature from sketch text. |
| [Create sheet metal face and fold features](../../sample-programs/FoldFeatures_Add_Sample.md) | This sample demonstrates the creation of sheet metal face and fold features. |
| [Hole Feature - Through holes (RegularAndTapped)](../../sample-programs/HoleFeature_Sample.md) | This sample demonstrates the creation of through holes, both regular and tapped. |
| [Create and Edit an Extrude Feature with a pocket](../../sample-programs/PartFeature_SetEndOfPart_Sample.md) | This sample demonstrates how to edit an extrude feature. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Sketch from Face Silhouette](../../sample-programs/PlanarSketch_AddBySilhouette_Sample.md) | This sample creates a cylindrical solid, creates a new sketch plane and creates some new sketch lines from the actual edges and the apparent (silhouette) edges of the cylinder. |
| [Querying a sketch profile to get regions.](../../sample-programs/Profile_RegionProperties_Sample.md) | This sample demonstrates getting region properties from a sketch profile. |
| [Sketch profile control](../../sample-programs/ProfilePath_AddsMaterial_Sample.md) | This sample demonstrates the usage of the Profiles API to control the shape of the profile. The sample creates three concntric circles and creates an extrusion of the region between the inner circles. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |
| [Thread Feature Create](../../sample-programs/ThreadFeature_Sample.md) | This sample demonstrates the creation of a thread feature. It creates a cylinder in a new part document and creates a thread feature on the cylinder. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |