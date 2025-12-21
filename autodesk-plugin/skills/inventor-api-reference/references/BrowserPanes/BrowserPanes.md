# BrowserPanes Object

## Description

The BrowserPanes object provides access to the existing objects of the browser and allows you to create additional panes. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../BrowserPanes/BrowserPanes_Add.md) | Method that creates and returns a new BrowserPane object. The BrowserPane created is one that is explicitly used to house ActiveX controls. |
| [AddByManifest](../BrowserPanes/BrowserPanes_AddByManifest.md) | Method that creates and returns a new BrowserPane object. The BrowserPane created is one that is explicitly used to house un-registered ActiveX Controls. |
| [AddTreeBrowserPane](../BrowserPanes/BrowserPanes_AddTreeBrowserPane.md) | Method that creates and returns a new BrowserPane object. The BrowserPane created is one in which Inventor's BrowserTreeNodes can be instanced to generate a completely customizable tree view. |
| [CreateBrowserNodeDefinition](../BrowserPanes/BrowserPanes_CreateBrowserNodeDefinition.md) | Method that creates a new The definition object can then be further used to construct ClientBrowserNodes that make up the tree in a custom tree-browser pane. The new ClientBrowserNodeDefinition is returned. Note that this node definition object is constructed and has an identity within the 'name space' or context of the entire owning document. |
| [GetClientBrowserNodeDefinition](../BrowserPanes/BrowserPanes_GetClientBrowserNodeDefinition.md) | Method that returns the specified ClientBrowserNodeDefinition. |
| [GetNativeBrowserNodeDefinition](../BrowserPanes/BrowserPanes_GetNativeBrowserNodeDefinition.md) | Method to obtain the NativeBrowserNodeDefinition object corresponding to a data model object.Also see CreateNativeBrowserNodeDefinition for information on creating a new client browser node definition. |
| [GetNativeBrowserNodeDefinitionWithOptions](../BrowserPanes/BrowserPanes_GetNativeBrowserNodeDefinitionWithOptions.md) | Method that returns the NativeBrowserNodeDefinition that corresponds to the input object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActivePane](../BrowserPanes/BrowserPanes_ActivePane.md) | Property that returns the that is currently being displayed. |
| [Application](../BrowserPanes/BrowserPanes_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BrowserPanesEvents](../BrowserPanes/BrowserPanes_BrowserPanesEvents.md) | Property that returns the events sink object for the BrowserPanes object. |
| [ClientNodeResources](../BrowserPanes/BrowserPanes_ClientNodeResources.md) | Property that returns the collection of ClientNodeResource objects. A ClientNodeResource holds the icons necessary to define the open, closed and status images for all of the ClientBrowserNodes associated with this document. The ClientNodeResources collection has a method that allows you to add a new set of images that can then be used to create a new ClientBrowserNodeDefinition. |
| [Count](../BrowserPanes/BrowserPanes_Count.md) | Property that returns the number of browser panes in the collection. |
| [Item](../BrowserPanes/BrowserPanes_Item.md) | Returns the specified object from the collection. |
| [Type](../BrowserPanes/BrowserPanes_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyDocument.BrowserPanes](../AssemblyDocument/AssemblyDocument_BrowserPanes.md), [Document.BrowserPanes](../Document/Document_BrowserPanes.md), [DrawingDocument.BrowserPanes](../DrawingDocument/DrawingDocument_BrowserPanes.md), [PartDocument.BrowserPanes](../PartDocument/PartDocument_BrowserPanes.md), [PresentationDocument.BrowserPanes](../PresentationDocument/PresentationDocument_BrowserPanes.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add assembly occurrences to a new folder](../../sample-programs/BrowserPaneObject_AddBrowserFolder_Sample.md) | Demonstrates assembly occurrences to a new folder |
| [Demote occurence](../../sample-programs/BrowserPaneObject_Reorder_Demote_Sample.md) | This sample demonstrates how to demote a top level occurrence in an assembly into a new sub-assembly occurrence. |
| [Navigation between browser and data](../../sample-programs/BrowserPanes_GetNativeBrowserNodeDefinition_Sample.md) | This sample demonstrates the navigation between a browser node and it's corresponding data model object and vice versa. This sample creates a work plane, finds its browser node and gets the work plane object back from the browser node. |

## Version

Introduced in version 5
