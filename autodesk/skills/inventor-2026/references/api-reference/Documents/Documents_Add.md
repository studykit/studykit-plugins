# Documents.Add Method

Parent Object: [Documents](../Documents/Documents.md)

## Description

Creates a new of the specified type. Optionally, a template file can be specified instead.

## Syntax

Documents.**Add**( ***DocumentType*** As [DocumentTypeEnum](../DocumentTypeEnum.md), [***TemplateFileName***] As String, [***CreateVisible***] As Boolean ) As [Document](../Document/Document.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentType | [DocumentTypeEnum](../DocumentTypeEnum.md) | Input DocumentTypeEnum that specifies the type of document to add. |
| TemplateFileName | String | Optional input String that specifies the name of the template file. The FileManager.GetTemplateFile can be used to get a template full file name. If not specified a document without template will be created. |
| CreateVisible | Boolean | Optional input Boolean that specifies whether the created document or template is visible.   This is an optional argument whose default value is True. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding iAssembly occurrences](../../sample-programs/AddiAssemblyMember_Sample.md) | This sample demonstrates adding iAssembly occurrences to an assembly. |
| [Adding iPart occurrences to an assembly](../../sample-programs/AddiPartMember_Sample.md) | This sample demonstrates adding iPart occurrences to an assembly. |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [Navigation between browser and data](../../sample-programs/BrowserPanes_GetNativeBrowserNodeDefinition_Sample.md) | This sample demonstrates the navigation between a browser node and it's corresponding data model object and vice versa. This sample creates a work plane, finds its browser node and gets the work plane object back from the browser node. |
| [Creating a new parameter group](../../sample-programs/CustomParameterGroup_Add_Sample.md) | This sample demonstrates the creation of model, reference and user parameters and copying these parameters to a newly created group. |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |
| [Extrude Feature - Create Block with Pocket](../../sample-programs/ExtrudeFeature_Sample.md) | This sample demonstrates creating a simple solid consisting a block with a pocket. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Hole Feature - Through holes (RegularAndTapped)](../../sample-programs/HoleFeature_Sample.md) | This sample demonstrates the creation of through holes, both regular and tapped. |

## Version

Introduced in version 4
