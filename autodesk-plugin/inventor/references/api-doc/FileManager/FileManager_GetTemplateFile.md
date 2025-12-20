# FileManager.GetTemplateFile Method

Parent Object: [FileManager](../FileManager/FileManager.md)

## Description

Method that specifies the template to use when creating a file.

## Syntax

FileManager.**GetTemplateFile**( ***DocumentType*** As [DocumentTypeEnum](../DocumentTypeEnum.md), [***SystemOfMeasure***] As [SystemOfMeasureEnum](../SystemOfMeasureEnum.md), [***DraftingStandard***] As [DraftingStandardEnum](../DraftingStandardEnum.md), [***DocumentSubType***] As Variant ) As String

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentType | [DocumentTypeEnum](../DocumentTypeEnum.md) | Input constant that specifies the type of document. |
| SystemOfMeasure | [SystemOfMeasureEnum](../SystemOfMeasureEnum.md) | Input constant that specifies the system of measure to use in the drawing being created.  If the DocumentType argument is specified to be kDrawingDocumentObject, the method will honor the application option Default Drawing File Type (equivalent to DrawingOptions.DefaultDrawingFileType) to decide whether to use an idw template or an Inventor DWG template. |
| DraftingStandard | [DraftingStandardEnum](../DraftingStandardEnum.md) | Input constant that specifies the drafting standard to use in the drawing being created.     This is an optional argument whose default value is 9729. |
| DocumentSubType | Variant | Input constant (GUID) that specifies the subtype of the document to be created (sheet metal or weldment).   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Creating a new parameter group](../../sample-programs/CustomParameterGroup_Add_Sample.md) | This sample demonstrates the creation of model, reference and user parameters and copying these parameters to a newly created group. |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |
| [Extrude Feature - Create Block with Pocket](../../sample-programs/ExtrudeFeature_Sample.md) | This sample demonstrates creating a simple solid consisting a block with a pocket. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Edit profile of an extrude feature](../../sample-programs/ExtrudeFeature_Profile_Sample.md) | This sample demonstrates editing the profile of an extrude feature. |
| [Create sheet metal face and fold features](../../sample-programs/FoldFeatures_Add_Sample.md) | This sample demonstrates the creation of sheet metal face and fold features. |
| [Hole Feature - Through holes (RegularAndTapped)](../../sample-programs/HoleFeature_Sample.md) | This sample demonstrates the creation of through holes, both regular and tapped. |
| [Create sheet metal lofted flange feature](../../sample-programs/LoftedFlangeFeatures_Add_Sample.md) | The following sample demonstrates the creation of a sheet metal lofted flange feature. |
| [Create and Edit an Extrude Feature with a pocket](../../sample-programs/PartFeature_SetEndOfPart_Sample.md) | This sample demonstrates how to edit an extrude feature. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Sketch from Face Silhouette](../../sample-programs/PlanarSketch_AddBySilhouette_Sample.md) | This sample creates a cylindrical solid, creates a new sketch plane and creates some new sketch lines from the actual edges and the apparent (silhouette) edges of the cylinder. |
| [Sketch profile control](../../sample-programs/ProfilePath_AddsMaterial_Sample.md) | This sample demonstrates the usage of the Profiles API to control the shape of the profile. The sample creates three concntric circles and creates an extrusion of the region between the inner circles. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Sheet Metal Feature Display](../../sample-programs/SheetMetalComponentDefinition_Sample.md) | This sample illustrates getting basic information from the various sheet metal features. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |