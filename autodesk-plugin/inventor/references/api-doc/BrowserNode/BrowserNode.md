# BrowserNode Object

## Description

The BrowserNode object represents a node in the browser.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddChild](../BrowserNode/BrowserNode_AddChild.md) | Method that creates a new as a nested child of this one. The new BrowserNode is returned. |
| [AllReferencedNodes](../BrowserNode/BrowserNode_AllReferencedNodes.md) | Method that returns all browser nodes referencing the specified BrowserNodeDefinition below this BrowserNode. For instance, in the case of a shared sketch, two browser nodes reference the same definition. |
| [Delete](../BrowserNode/BrowserNode_Delete.md) | Method that deletes the browser node. All of its child browser nodes are deleted as well. None of the corresponding browser node definitions nor the client node resources are deleted, however. This method will fail for built-in browser nodes. |
| [DoPreSelect](../BrowserNode/BrowserNode_DoPreSelect.md) | This method will simulate a mouse hover on the browser node. |
| [DoSelect](../BrowserNode/BrowserNode_DoSelect.md) | This method will simulate a mouse click on the browser node. |
| [EnsureVisible](../BrowserNode/BrowserNode_EnsureVisible.md) | Method that ensures the BrowserNode object is visible. |
| [InsertChild](../BrowserNode/BrowserNode_InsertChild.md) | Method that creates a new BrowserNode at the specified location. The new BrowserNode is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BrowserNode/BrowserNode_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BrowserFolders](../BrowserNode/BrowserNode_BrowserFolders.md) | Property that returns a collection of all browser folders contained directly under this node in the browser. |
| [BrowserNodeDefinition](../BrowserNode/BrowserNode_BrowserNodeDefinition.md) | Property that returns a object which defines the various inputs that were used to create the browser node. |
| [BrowserNodes](../BrowserNode/BrowserNode_BrowserNodes.md) | Property that returns a collection of the top level BrowserNode objects contained under this node. |
| [Expanded](../BrowserNode/BrowserNode_Expanded.md) | Specifies the BrowserNode object is expanded. |
| [FullPath](../BrowserNode/BrowserNode_FullPath.md) | Gets the fully qualified label of the BrowserNode. |
| [NativeObject](../BrowserNode/BrowserNode_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../BrowserNode/BrowserNode_Parent.md) | Property that returns the parent of the BrowserNode object. This may either be another BrowserNode or a BrowserPane. |
| [Selected](../BrowserNode/BrowserNode_Selected.md) | Property that returns whether the object is selected or not. |
| [Type](../BrowserNode/BrowserNode_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../BrowserNode/BrowserNode_Visible.md) | Gets and sets whether the browser node is visible or not. |

## Accessed From

[BrowserFolder.BrowserNode](../BrowserFolder/BrowserFolder_BrowserNode.md), [BrowserNode.AddChild](../BrowserNode/BrowserNode_AddChild.md), [BrowserNode.InsertChild](../BrowserNode/BrowserNode_InsertChild.md), [BrowserNodesEnumerator.Item](../BrowserNodesEnumerator/BrowserNodesEnumerator_Item.md), [BrowserNodesEnumerator.ItemById](../BrowserNodesEnumerator/BrowserNodesEnumerator_ItemById.md), [BrowserPane.GetBrowserNodeFromObject](../BrowserPane/BrowserPane_GetBrowserNodeFromObject.md), [BrowserPane.TopNode](../BrowserPane/BrowserPane_TopNode.md), [ClientFeature.BrowserNode](../ClientFeature/ClientFeature_BrowserNode.md), [ClientFeatureProxy.BrowserNode](../ClientFeatureProxy/ClientFeatureProxy_BrowserNode.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add assembly occurrences to a new folder](../../sample-programs/BrowserPaneObject_AddBrowserFolder_Sample.md) | Demonstrates assembly occurrences to a new folder |
| [Demote occurence](../../sample-programs/BrowserPaneObject_Reorder_Demote_Sample.md) | This sample demonstrates how to demote a top level occurrence in an assembly into a new sub-assembly occurrence. |
| [Navigation between browser and data](../../sample-programs/BrowserPanes_GetNativeBrowserNodeDefinition_Sample.md) | This sample demonstrates the navigation between a browser node and it's corresponding data model object and vice versa. This sample creates a work plane, finds its browser node and gets the work plane object back from the browser node. |

## Version

Introduced in version 8

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |