# EnvironmentManager Object

## Description

This object provides methods and properties to get and set the base and override environments for this document. For more information, refer to the [Environments overviews](Environments_Overview.md).

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetCurrentEnvironment](../EnvironmentManager/EnvironmentManager_GetCurrentEnvironment.md) | Method that gets the current Environment for this document. This is the environment that the document is currently displayed in. |
| [SetCurrentEnvironment](../EnvironmentManager/EnvironmentManager_SetCurrentEnvironment.md) | Method that sets the current Environment for this document. This is the environment that the document is currently displayed in. The change is not persisted with the document; i.e. the next time the document is opened, it will show up in its base environment or the override environment if specified. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../EnvironmentManager/EnvironmentManager_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BaseEnvironment](../EnvironmentManager/EnvironmentManager_BaseEnvironment.md) | Property that returns the Environment that is defined as the default for this document. This is the environment displayed when the document is opened unless an override environment has been specified for this document. |
| [EditObjectEnvironment](../EnvironmentManager/EnvironmentManager_EditObjectEnvironment.md) | This method returns the environment associated with the currently active edit object. This is the environment which is the topmost entry in the Application menu. Since Autodesk Inventor 10, the active environment and EditObjectEnvironment are not necessarily the same. Using parallel environments, one can switch to a parallel environment for the same edit object. |
| [OverrideEnvironment](../EnvironmentManager/EnvironmentManager_OverrideEnvironment.md) | Gets and sets the current override environment for this document. |
| [Parent](../EnvironmentManager/EnvironmentManager_Parent.md) | Property that returns the parent of the EnvironmentManager. |
| [Type](../EnvironmentManager/EnvironmentManager_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyDocument.EnvironmentManager](../AssemblyDocument/AssemblyDocument_EnvironmentManager.md), [DrawingDocument.EnvironmentManager](../DrawingDocument/DrawingDocument_EnvironmentManager.md), [PartDocument.EnvironmentManager](../PartDocument/PartDocument_EnvironmentManager.md), [PresentationDocument.EnvironmentManager](../PresentationDocument/PresentationDocument_EnvironmentManager.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Play back a simulation](../../sample-programs/DesignSimulation_PlaySimulation_Sample.md) | This sample plays back an existing dynamic simulation. |
| [Creation of an override environment for a document](../../sample-programs/EnvironmentManager_OverrideEnvironment_Sample.md) | A new ribbon tab is created and associated with the override environment. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |