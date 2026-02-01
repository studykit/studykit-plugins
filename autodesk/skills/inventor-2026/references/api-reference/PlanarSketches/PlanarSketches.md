# PlanarSketches Object

## Description

The PlanarSketches collection object provides access to all of the objects and provides methods to create additional PlanarSketch objects. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../PlanarSketches/PlanarSketches_Add.md) | Method that creates a new sketch based on the input planar entity. |
| [AddWithOrientation](../PlanarSketches/PlanarSketches_AddWithOrientation.md) | Method that creates a new sketch based on the input planar entity and orientation information. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PlanarSketches/PlanarSketches_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../PlanarSketches/PlanarSketches_Count.md) | Property that returns the number of items in this collection. |
| [Item](../PlanarSketches/PlanarSketches_Item.md) | Allows integer-indexed access to items in the collection. |
| [Type](../PlanarSketches/PlanarSketches_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyComponentDefinition.Sketches](../AssemblyComponentDefinition/AssemblyComponentDefinition_Sketches.md), [FlatPattern.Sketches](../FlatPattern/FlatPattern_Sketches.md), [PartComponentDefinition.Sketches](../PartComponentDefinition/PartComponentDefinition_Sketches.md), [SheetMetalComponentDefinition.Sketches](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_Sketches.md), [WeldmentComponentDefinition.Sketches](../WeldmentComponentDefinition/WeldmentComponentDefinition_Sketches.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |
| [Using Inventor's error dialog](../../sample-programs/ErrorManager_Sample.md) | Demonstrates using Inventor's error dialog. |
| [Extrude Feature - Create Block with Pocket](../../sample-programs/ExtrudeFeature_Sample.md) | This sample demonstrates creating a simple solid consisting a block with a pocket. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Edit profile of an extrude feature](../../sample-programs/ExtrudeFeature_Profile_Sample.md) | This sample demonstrates editing the profile of an extrude feature. |
| [Create sheet metal face and fold features](../../sample-programs/FoldFeatures_Add_Sample.md) | This sample demonstrates the creation of sheet metal face and fold features. |
| [Hole Feature - Through holes (RegularAndTapped)](../../sample-programs/HoleFeature_Sample.md) | This sample demonstrates the creation of through holes, both regular and tapped. |
| [Create and Edit an Extrude Feature with a pocket](../../sample-programs/PartFeature_SetEndOfPart_Sample.md) | This sample demonstrates how to edit an extrude feature. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Sketch Edit Orientation](../../sample-programs/PlanarSketch_NaturalAxisDirection_Sample.md) | This sample demonstrates modifying the orientation of a sketch. |
| [Sketch Add](../../sample-programs/PlanarSketches_Add_Sample.md) | This sample demonstrates the creation of a sketch using the Sketches.Add method. |
| [Sketch Add Oriented](../../sample-programs/PlanarSketches_AddWithOrientation_Sample.md) | This sample demonstrates the creation of a sketch using the Sketches.AddWithOrientation method. |
| [Sketch profile control](../../sample-programs/ProfilePath_AddsMaterial_Sample.md) | This sample demonstrates the usage of the Profiles API to control the shape of the profile. The sample creates three concntric circles and creates an extrusion of the region between the inner circles. |
| [Add a punch tool feature](../../sample-programs/PunchToolFeatures_Add_Sample.md) | This program demonstrates the creation of a punch tool feature. It uses one of the punch features that's delivered with Inventor. It assumes you already have an existing sheet metal part and have selected a face to place the punch feature on. The selected face should be large so there is room for the punch features. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |
| [Projection - project across parts](../../sample-programs/Sketch_AddByProjectingEntity_Sample.md) | This sample demonstrates projecting a sketch entity across parts in an assembly. To use the sample, have an assembly open that contains at least two occurrences, (parts only), and run the program. |
| [Sketch Delete](../../sample-programs/Sketch_Delete_Sample.md) | This sample demonstrates deleting a sketch. |
| [Sketch Open for Edit](../../sample-programs/Sketch_Edit_Sample.md) | This sample demonstrates opening a sketch for edit. |
| [Set Sketch Visibility](../../sample-programs/Sketch_Visible_Sample.md) | This sample demonstrates setting the visibility of a sketch. |
| [Create and insert a sketch block definition into a part sketch](../../sample-programs/SketchBlockDefinition_Sample.md) | This sample demonstrates inserting a sketch block into a part sketch. |
| [Create sketch block from an existing sketch](../../sample-programs/SketchBlocks_Add_Sample.md) | This sample demonstrates creating a sketch block from an existing sketch. |
| [Spline - create NURBS](../../sample-programs/SketchFixedSpline_Sample.md) | This sample demonstrates the creation of a sketch spline using a geometry definition (a NURB). The API also supports creation of 3D sketch splines in a similar way. |

## Version

Introduced in version 5
