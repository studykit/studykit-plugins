# Workspace Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Workspace.h>

## Description

A Workspace provides access to a set of panels, which contain commands that are relevant for that particular workspace. The user can switch from one workspace to another in a product (e.g. switch from Model to Sculpt in Fusion).

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [activate](Workspace_activate.htm) | Activate the workspace (assuming it is valid to do so - a SIM workspace can't be activated if Fusion is the active product). |
| [classType](Workspace_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](Workspace_deleteMe.htm) | Deletes this workspace. Only a workspace added by the API can be deleted, (IsNative is false). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [id](Workspace_id.htm) | Gets the unique Id of the workspace that can be used programmatically to find a specific workspace. It is not affected by the current language. |
| [isActive](Workspace_isActive.htm) | Gets if the workspace is currently active - i.e. displayed |
| [isNative](Workspace_isNative.htm) | Gets if this workspace is native to Fusion or was created via the API. |
| [isValid](Workspace_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](Workspace_name.htm) | Gets the visible name of the workspace as seen in the user interface. This is the localized name. |
| [objectType](Workspace_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [productType](Workspace_productType.htm) | Returns the name of the product this workspace is associated with. |
| [resourceFolder](Workspace_resourceFolder.htm) | Gets or sets the resource folder. |
| [toolbarPanels](Workspace_toolbarPanels.htm) | Gets the collection containing the panels associated with this workspace. It's through this collection that you can add new toolbar panels. |
| [toolbarTabs](Workspace_toolbarTabs.htm) | Gets the collection containing the tabs associated with this workspace. |
| [toolClipFilename](Workspace_toolClipFilename.htm) | Gets or sets the full filename of the image file (PNG) used for the tool clip. the tool clip is the image shown when the user hovers the mouse over the workspace name in the workspace drop-down. |
| [tooltip](Workspace_tooltip.htm) | Gets or sets the tooltip text displayed for the workspace. This is the first line of text shown when the user hovers over the workspace name in the Fusion toolbar drop-down. This is typically the name of the workspace. This is different from the name in the that the name is a short name shown in the drop-down. The tooltip is only shown when the user hovers over the name and box appears providing more information about the workspace. For example, the name of the model workspace is "Model" and the tooltip is "Model Workspace". |
| [tooltipDescription](Workspace_tooltipDescription.htm) | Gets or sets the tooltip description displayed for the workspace. The tooltip description is a longer description of the workspace and is only displayed when the user hovers over the workspace name in the Fusion toolbar drop-down. The pop-up dialog that appears contains the tooltip, the tooltip description, and the tool clip which is a picture. |

## Accessed From

[UserInterface.activeWorkspace](UserInterface_activeWorkspace.htm), [WorkspaceEventArgs.workspace](WorkspaceEventArgs_workspace.htm), [WorkspaceList.item](WorkspaceList_item.htm), [WorkspaceList.itemById](WorkspaceList_itemById.htm), [Workspaces.item](Workspaces_item.htm), [Workspaces.itemById](Workspaces_itemById.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Customizing the UI using the API Sample](UICustomizationSample_Sample.htm) | Demonstrates how to work with tabs, panels, and command in the user interface. The full source for [C++](../ExtraFiles/UICustomizationSampleCPP.zip) and [Python](../ExtraFiles/UICustomizationSamplePython.zip) samples can be downloaded. This is especially useful for getting the resource files. |
| [Write user interface to a file API Sample](WriteUserInterfaceToFile_Sample.htm) | Writes out the full structure of the Fusion user interface. This information is useful when editing the user-interface, as discussed in the usre manual topic [User-Interface Customization with Fusion's API](UserInterface_UM.htm) |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |