# BrowserFolder.Add Method

Parent Object: [BrowserFolder](../BrowserFolder/BrowserFolder.md)

## Description

Method that adds a node to the folder. The node is automatically reordered in the browser if required. If the node cannot be reordered as needed, the method returns an error.

## Syntax

BrowserFolder.**Add**( ***BrowserNode*** As [BrowserNode](../BrowserNode/BrowserNode.md), [***TargetNode***] As Variant, [***Before***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BrowserNode | [BrowserNode](../BrowserNode/BrowserNode.md) | Input BrowserNode object that specifies the object to be moved into the folder. |
| TargetNode | Variant | Optional input BrowserNode object that specifies the object within the folder adjacent to which the input node should be positioned. This node should be found directly under the folder, else the method returns an error. If not specified, the node is added to the top of the list in the folder. |
| Before | Boolean | Optional input Boolean that specifies whether the input node should be moved before or after the target node. If not specified, the node is positioned after the target node. This argument is ignored if the TargetNode argument is not specified.   This is an optional argument whose default value is False. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |