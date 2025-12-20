# BrowserFolder.Remove Method

Parent Object: [BrowserFolder](../BrowserFolder/BrowserFolder.md)

## Description

Method that removes a node from the folder. The node is automatically reordered in the browser if required. If the node cannot be reordered as needed, the method returns an error.

## Syntax

BrowserFolder.**Remove**( ***BrowserNode*** As [BrowserNode](../BrowserNode/BrowserNode.md), [***TargetNode***] As Variant, [***Before***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BrowserNode | [BrowserNode](../BrowserNode/BrowserNode.md) | Input BrowserNode object that specifies the object to be removed from the folder. |
| TargetNode | Variant | Optional input BrowserNode object that specifies the object outside the folder adjacent to which the input node should be positioned. If not specified, the node is positioned adjacent to the folder (either before or after). |
| Before | Boolean | Optional input Boolean that specifies whether the input node should be moved before or after the target node. If not specified, the node is positioned after the target node.   This is an optional argument whose default value is False. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |