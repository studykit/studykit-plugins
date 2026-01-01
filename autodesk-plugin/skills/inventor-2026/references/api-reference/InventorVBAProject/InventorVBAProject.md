# InventorVBAProject Object

## Description

Represents Autodesk Inventor's VBA project.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Close](../InventorVBAProject/InventorVBAProject_Close.md) | Method that closes this project. Please note that this method works only for user-defined VBA projects. It will not work with Application or Document VBA projects, which are built in. |
| [Save](../InventorVBAProject/InventorVBAProject_Save.md) | Method that saves the VBA project. |
| [SaveAs](../InventorVBAProject/InventorVBAProject_SaveAs.md) | Method that saves the project to a specified location. Please note that this method works only for user-defined VBA projects. It will not work with Application or Document VBA projects, which are built in. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [InventorVBAComponents](../InventorVBAProject/InventorVBAProject_InventorVBAComponents.md) | Gets the InventorVBAComponents contained in this project. |
| [Name](../InventorVBAProject/InventorVBAProject_Name.md) | Gets/Sets the projects display name. |
| [Parent](../InventorVBAProject/InventorVBAProject_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [ProjectType](../InventorVBAProject/InventorVBAProject_ProjectType.md) | Property that returns a constant specifying the type of VBA project this project is. |
| [Saved](../InventorVBAProject/InventorVBAProject_Saved.md) | Property that indicates if this project has been saved or not. |
| [Type](../InventorVBAProject/InventorVBAProject_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [VBProject](../InventorVBAProject/InventorVBAProject_VBProject.md) | Property that returns the VBA project that corresponds to this InventorVBAProject. |

## Accessed From

[AssemblyDocument.VBAProject](../AssemblyDocument/AssemblyDocument_VBAProject.md), [Document.VBAProject](../Document/Document_VBAProject.md), [DrawingDocument.VBAProject](../DrawingDocument/DrawingDocument_VBAProject.md), [InventorVBAComponent.Parent](../InventorVBAComponent/InventorVBAComponent_Parent.md), [InventorVBAComponents.Parent](../InventorVBAComponents/InventorVBAComponents_Parent.md), [InventorVBAProjects.Add](../InventorVBAProjects/InventorVBAProjects_Add.md), [InventorVBAProjects.Item](../InventorVBAProjects/InventorVBAProjects_Item.md), [PartDocument.VBAProject](../PartDocument/PartDocument_VBAProject.md), [PresentationDocument.VBAProject](../PresentationDocument/PresentationDocument_VBAProject.md)

## Version

Introduced in version 6
