# ExtrudeFeatures.CreateExtrudeDefinition Method

Parent Object: [ExtrudeFeatures](../ExtrudeFeatures/ExtrudeFeatures.md)

## Description

Method that creates a new ExtrudeDefinition object. The object created does not represent an extrude feature but instead is a representation of the information that defines an extrude feature. You can use this object as input to the ExtrudeFeatures.Add method to create the actual feature.

## Remarks

The ExtrudeDefinition object returned is fully defined and can be used to create an extrude feature. However, defaults are used for extrude options (including a distance extent type with a value of “1.0 in”), so you may want to change some of the property values of the ExtrudeDefinition object before using it to create a feature.

## Syntax

ExtrudeFeatures.**CreateExtrudeDefinition**( ***Profile*** As [Profile](../Profile/Profile.md), ***Operation*** As [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) ) As [ExtrudeDefinition](../ExtrudeDefinition/ExtrudeDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Profile | [Profile](../Profile/Profile.md) | Input Profile object that specifies the sketch profile to use for the extrude feature. |
| Operation | [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) | Input that specifies the type of operation used to add the feature to the model. Valid inputs are kNewBodyOperation, kJoinOperation, kCutOperation, kIntersectOperation and kSurfaceOperation. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |
| [Using Inventor's error dialog](../../sample-programs/ErrorManager_Sample.md) | Demonstrates using Inventor's error dialog. |
| [Extrude Feature - Create Block with Pocket](../../sample-programs/ExtrudeFeature_Sample.md) | This sample demonstrates creating a simple solid consisting a block with a pocket. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Edit profile of an extrude feature](../../sample-programs/ExtrudeFeature_Profile_Sample.md) | This sample demonstrates editing the profile of an extrude feature. |
| [Extrude sketch text](../../sample-programs/ExtrudeFeatures_AddByDistanceExtent_Sample.md) | This sample demonstrates the creation of an extrude feature from sketch text. |
| [Add iMate Definition](../../sample-programs/iMateDefinitions_AddMateiMateDefinition_Sample.md) | Add iMate definitions using AddMateiMateDefinition and AddInsertiMateDefinition. |
| [Create and Edit an Extrude Feature with a pocket](../../sample-programs/PartFeature_SetEndOfPart_Sample.md) | This sample demonstrates how to edit an extrude feature. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Sketch from Face Silhouette](../../sample-programs/PlanarSketch_AddBySilhouette_Sample.md) | This sample creates a cylindrical solid, creates a new sketch plane and creates some new sketch lines from the actual edges and the apparent (silhouette) edges of the cylinder. |
| [Sketch profile control](../../sample-programs/ProfilePath_AddsMaterial_Sample.md) | This sample demonstrates the usage of the Profiles API to control the shape of the profile. The sample creates three concntric circles and creates an extrusion of the region between the inner circles. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Thread Feature Create](../../sample-programs/ThreadFeature_Sample.md) | This sample demonstrates the creation of a thread feature. It creates a cylinder in a new part document and creates a thread feature on the cylinder. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |