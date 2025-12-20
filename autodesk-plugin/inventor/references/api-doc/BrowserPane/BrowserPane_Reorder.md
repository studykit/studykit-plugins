# BrowserPane.Reorder Method

Parent Object: [BrowserPane](../BrowserPane/BrowserPane.md)

## Description

Moves a node or group of nodes to a new target position within the browser pane.

## Syntax

BrowserPane.**Reorder**( ***TargetNode*** As [BrowserNode](../BrowserNode/BrowserNode.md), ***Before*** As Boolean, ***StartNode*** As [BrowserNode](../BrowserNode/BrowserNode.md), [***EndNode***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TargetNode | [BrowserNode](../BrowserNode/BrowserNode.md) | Input BrowserNode object to position the browser nodes next to. An error will occur if the target node is not at the same level in the browser as the node(s) being repositioned. The input node must belong to this pane. |
| Before | Boolean | Input Boolean that indicates whether to position the node(s) before or after the target browser node. A value of True indicates that the node(s) will be positioned before the target node. |
| StartNode | [BrowserNode](../BrowserNode/BrowserNode.md) | Input BrowserNode object that specifies the node to be repositioned. The input node must belong to this pane. |
| EndNode | Variant | Optional input BrowserNode object. If specified, all the browser node objects from the StartNode to the EndNode, both inclusive, will be repositioned to the specified position in the tree. If not specified, only the StartNode will be repositioned. This argument is currently ignored in drawings. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Demote occurence](../../sample-programs/BrowserPaneObject_Reorder_Demote_Sample.md) | This sample demonstrates how to demote a top level occurrence in an assembly into a new sub-assembly occurrence. |
| [Promote occurence](../../sample-programs/BrowserPaneObject_Reorder_Promote_Sample.md) | This sample demonstrates how to promote an occurrence. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |