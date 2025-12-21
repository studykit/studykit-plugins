# BrowserFolder Object

## Description

The BrowserFolder object represents a folder in the browser.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../BrowserFolder/BrowserFolder_Add.md) | Method that adds a node to the folder. The node is automatically reordered in the browser if required. If the node cannot be reordered as needed, the method returns an error. |
| [Delete](../BrowserFolder/BrowserFolder_Delete.md) | Method that deletes the browser folder. The contents of the folder are retained and moved up one level in the browser. |
| [GetReferenceKey](../BrowserFolder/BrowserFolder_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |
| [Remove](../BrowserFolder/BrowserFolder_Remove.md) | Method that removes a node from the folder. The node is automatically reordered in the browser if required. If the node cannot be reordered as needed, the method returns an error. |
| [SetEndOfPart](../BrowserFolder/BrowserFolder_SetEndOfPart.md) | Method that moves the end of part before or after the folder. The method only applies for first level folders in part documents and first level folders in the features portion of the browser in assembly documents. The method returns an error for all other folders. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllowAddRemove](../BrowserFolder/BrowserFolder_AllowAddRemove.md) | Read-write property that gets and sets whether items can be added to and removed from the folder by the user. If set to False, the add/remove restriction applies to the user interface only - the contents of folder can still be modified via the API. |
| [AllowDelete](../BrowserFolder/BrowserFolder_AllowDelete.md) | Read-write property that gets and sets whether the folder can be deleted by the user. If set to False, the delete restriction applies to the user interface only - the folder can still be deleted via the API. |
| [AllowRename](../BrowserFolder/BrowserFolder_AllowRename.md) | Read-write property that gets and sets whether the folder can be renamed by the user. If set to False, the rename restriction applies to the user interface only - the folder can still be renamed via the API. |
| [AllowReorder](../BrowserFolder/BrowserFolder_AllowReorder.md) | Read-write property that gets and sets whether the folder can be reordered in the browser by the user. If set to False, the reorder restriction applies to the user interface only - the folder can still be reordered via the API. |
| [Application](../BrowserFolder/BrowserFolder_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BrowserNode](../BrowserFolder/BrowserFolder_BrowserNode.md) | Property that returns the corresponding browser node for the folder. The contents of the folder (including sub-folders) can be accessed via the browser node. |
| [InternalName](../BrowserFolder/BrowserFolder_InternalName.md) | Read-only property that returns the unique internal name of the folder. |
| [Name](../BrowserFolder/BrowserFolder_Name.md) | Read-write property that gets and sets the name of the folder. |
| [Parent](../BrowserFolder/BrowserFolder_Parent.md) | Property that returns the parent browser node for the folder. |
| [Type](../BrowserFolder/BrowserFolder_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BrowserFoldersEnumerator.Item](../BrowserFoldersEnumerator/BrowserFoldersEnumerator_Item.md), [BrowserPane.AddBrowserFolder](../BrowserPane/BrowserPane_AddBrowserFolder.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add assembly occurrences to a new folder](../../sample-programs/BrowserPaneObject_AddBrowserFolder_Sample.md) | Demonstrates assembly occurrences to a new folder |

## Version

Introduced in version 2010
