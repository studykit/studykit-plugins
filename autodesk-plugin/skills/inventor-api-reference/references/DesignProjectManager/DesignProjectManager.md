# DesignProjectManager Object

## Description

The DesignProjectManager object provides access to project files related functionality in Inventor.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddOptionsButton](../DesignProjectManager/DesignProjectManager_AddOptionsButton.md) | Method that adds an options button to the Projects dialog. The returned button object can be used to receive an OnClick event fired when the user clicks the option button. |
| [IsFileInActiveProject](../DesignProjectManager/DesignProjectManager_IsFileInActiveProject.md) | Method that returns whether the given file is located within the active project using the resolution rules of the project, and additionally returns the path type (library, workspace, workgroup) and its name. |
| [ResolveFile](../DesignProjectManager/DesignProjectManager_ResolveFile.md) | Method that runs the file resolver from the source path and attempts to find the destination file name, in the active project. The full file name of the resolved file is returned. A null string is returned if no file was resolved to. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveDesignProject](../DesignProjectManager/DesignProjectManager_ActiveDesignProject.md) | Property that returns the currently active design project. Use DesignProject.Activate method to activate a project. |
| [Application](../DesignProjectManager/DesignProjectManager_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DesignProjects](../DesignProjectManager/DesignProjectManager_DesignProjects.md) | Property that returns the DesignProjects collection object containing all the projects. |
| [Parent](../DesignProjectManager/DesignProjectManager_Parent.md) | Property that returns the parent Application or ApprenticeServerComponent object. |
| [Type](../DesignProjectManager/DesignProjectManager_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Application.DesignProjectManager](../Application/Application_DesignProjectManager.md), [ApprenticeServer.DesignProjectManager](../ApprenticeServer/ApprenticeServer_DesignProjectManager.md), [ApprenticeServerComponent.DesignProjectManager](../ApprenticeServerComponent/ApprenticeServerComponent_DesignProjectManager.md), [DesignProject.Parent](../DesignProject/DesignProject_Parent.md), [InventorServer.DesignProjectManager](InventorServer_DesignProjectManager.md), [InventorServerObject.DesignProjectManager](InventorServerObject_DesignProjectManager.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Set active project](../../sample-programs/ProjectActivate_Sample.md) | The following sample demonstrates the activation of an Inventor project. |
| [Create project](../../sample-programs/ProjectCreation_Sample.md) | The following sample demonstrates the creation of an Inventor project. |
| [Query and create library paths](../../sample-programs/ProjectLibraryPaths_Sample.md) | The following sample demonstrates querying existing library paths associated with a project and adding a new library path. |

## Version

Introduced in version 2011
