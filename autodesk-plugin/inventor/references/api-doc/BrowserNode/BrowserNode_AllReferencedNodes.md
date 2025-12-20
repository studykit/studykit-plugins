# BrowserNode.AllReferencedNodes Method

Parent Object: [BrowserNode](../BrowserNode/BrowserNode.md)

## Description

Method that returns all browser nodes referencing the specified BrowserNodeDefinition below this BrowserNode. For instance, in the case of a shared sketch, two browser nodes reference the same definition.

## Syntax

BrowserNode.**AllReferencedNodes**( ***Definition*** As [BrowserNodeDefinition](../BrowserNodeDefinition/BrowserNodeDefinition.md) ) As [BrowserNodesEnumerator](../BrowserNodesEnumerator/BrowserNodesEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Definition | [BrowserNodeDefinition](../BrowserNodeDefinition/BrowserNodeDefinition.md) | Input BrowserNodeDefinition object to get the referenced nodes for. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Navigation between browser and data](../../sample-programs/BrowserPanes_GetNativeBrowserNodeDefinition_Sample.md) | This sample demonstrates the navigation between a browser node and it's corresponding data model object and vice versa. This sample creates a work plane, finds its browser node and gets the work plane object back from the browser node. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |