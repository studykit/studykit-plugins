# ImportedComponents.CreateDefinition Method

Parent Object: [ImportedComponents](../ImportedComponents/ImportedComponents.md)

## Description

Method that creates a new ImportedComponentDefinition object. The returned definition provides access to all of the items in the file that can be imported.

## Syntax

ImportedComponents.**CreateDefinition**( ***FullFileName*** As String ) As [ImportedComponentDefinition](../ImportedComponentDefinition/ImportedComponentDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input string that specifies the full filename of a CAD file. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Associatively import AutoCAD](../../sample-programs/ImportedComponent_AutoCAD_DWG_Sample.md) | This sample demonstrates how to import AutoCAD associatively. |
| [ImportedDWGComponent Creation](../../sample-programs/ImportedDWGComponentCreation_Sample.md) | This sample demonstrates how to create an imported DWG component into Inventor part document, and project the DWG entities onto Inventor planar sketch. |
| [Import Revit data into Inventor](../../sample-programs/ImportRevitIntoInventor_Sample.md) | The samples demonstrate how to import Revit data(.rvt) into Inventor part and assembly documents. |

## Version

Introduced in version 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |