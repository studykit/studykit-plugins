# PlanarSketches.Add Method

Parent Object: [PlanarSketches](../PlanarSketches/PlanarSketches.md)

## Description

Method that creates a new sketch based on the input planar entity.

## Syntax

PlanarSketches.**Add**( ***PlanarEntity*** As Object, [***UseFaceEdges***] As Boolean ) As [PlanarSketch](../PlanarSketch/PlanarSketch.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PlanarEntity | Object | Input object that defines the planar object the sketch is to be built on. Valid input for this argument includes planar faces and work planes. |
| UseFaceEdges | Boolean | Optional input Boolean that specifies if sketch geometry should automatically be created for all of the edges of the input face. This is the behavior when creating a sketch interactively in Autodesk Inventor. This argument is ignored in the case when PlanarEntity is a work plane. The default value of False specifies that no sketch geometry should automatically be created from the face edges. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Copy a sketch](../../sample-programs/CopySketch_Sample.md) | This sample demonstrates copying the contents of a sketch into another sketch via the API. |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |
| [Using Inventor's error dialog](../../sample-programs/ErrorManager_Sample.md) | Demonstrates using Inventor's error dialog. |
| [Extrude Feature - Create Block with Pocket](../../sample-programs/ExtrudeFeature_Sample.md) | This sample demonstrates creating a simple solid consisting a block with a pocket. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Edit profile of an extrude feature](../../sample-programs/ExtrudeFeature_Profile_Sample.md) | This sample demonstrates editing the profile of an extrude feature. |
| [Extrude sketch text](../../sample-programs/ExtrudeFeatures_AddByDistanceExtent_Sample.md) | This sample demonstrates the creation of an extrude feature from sketch text. |
| [Create sheet metal face and fold features](../../sample-programs/FoldFeatures_Add_Sample.md) | This sample demonstrates the creation of sheet metal face and fold features. |
| [Hole Feature - Through holes (RegularAndTapped)](../../sample-programs/HoleFeature_Sample.md) | This sample demonstrates the creation of through holes, both regular and tapped. |
| [Create and Edit an Extrude Feature with a pocket](../../sample-programs/PartFeature_SetEndOfPart_Sample.md) | This sample demonstrates how to edit an extrude feature. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Sketch from Face Silhouette](../../sample-programs/PlanarSketch_AddBySilhouette_Sample.md) | This sample creates a cylindrical solid, creates a new sketch plane and creates some new sketch lines from the actual edges and the apparent (silhouette) edges of the cylinder. |
| [Sketch Edit Orientation](../../sample-programs/PlanarSketch_NaturalAxisDirection_Sample.md) | This sample demonstrates modifying the orientation of a sketch. |
| [Sketch Add](../../sample-programs/PlanarSketches_Add_Sample.md) | This sample demonstrates the creation of a sketch using the Sketches.Add method. |
| [Sketch profile control](../../sample-programs/ProfilePath_AddsMaterial_Sample.md) | This sample demonstrates the usage of the Profiles API to control the shape of the profile. The sample creates three concntric circles and creates an extrusion of the region between the inner circles. |
| [Add a punch tool feature](../../sample-programs/PunchToolFeatures_Add_Sample.md) | This program demonstrates the creation of a punch tool feature. It uses one of the punch features that's delivered with Inventor. It assumes you already have an existing sheet metal part and have selected a face to place the punch feature on. The selected face should be large so there is room for the punch features. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |
| [Projection - project across parts](../../sample-programs/Sketch_AddByProjectingEntity_Sample.md) | This sample demonstrates projecting a sketch entity across parts in an assembly. To use the sample, have an assembly open that contains at least two occurrences, (parts only), and run the program. |
| [Create and insert a sketch block definition into a part sketch](../../sample-programs/SketchBlockDefinition_Sample.md) | This sample demonstrates inserting a sketch block into a part sketch. |
| [Create sketch block from an existing sketch](../../sample-programs/SketchBlocks_Add_Sample.md) | This sample demonstrates creating a sketch block from an existing sketch. |
| [Spline - create NURBS](../../sample-programs/SketchFixedSpline_Sample.md) | This sample demonstrates the creation of a sketch spline using a geometry definition (a NURB). The API also supports creation of 3D sketch splines in a similar way. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |

## Version

Introduced in version 5
