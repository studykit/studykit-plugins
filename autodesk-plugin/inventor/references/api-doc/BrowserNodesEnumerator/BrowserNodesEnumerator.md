# BrowserNodesEnumerator Object

## Description

This object provides access to the individual objects in a collection of nodes; for example the nested children of a given .

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ItemById](../BrowserNodesEnumerator/BrowserNodesEnumerator_ItemById.md) | Returns the specified object from the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BrowserNodesEnumerator/BrowserNodesEnumerator_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../BrowserNodesEnumerator/BrowserNodesEnumerator_Count.md) | Property that returns the number of items in the collection. Only the immediate children are counted. |
| [Item](../BrowserNodesEnumerator/BrowserNodesEnumerator_Item.md) | Returns the specified object from the collection. |
| [Type](../BrowserNodesEnumerator/BrowserNodesEnumerator_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BrowserNode.AllReferencedNodes](../BrowserNode/BrowserNode_AllReferencedNodes.md), [BrowserNode.BrowserNodes](../BrowserNode/BrowserNode_BrowserNodes.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Demote occurence](../../sample-programs/BrowserPaneObject_Reorder_Demote_Sample.md) | This sample demonstrates how to demote a top level occurrence in an assembly into a new sub-assembly occurrence. |

## Version

Introduced in version 8

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |