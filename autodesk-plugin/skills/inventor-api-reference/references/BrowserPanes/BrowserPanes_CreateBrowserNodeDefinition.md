# BrowserPanes.CreateBrowserNodeDefinition Method

Parent Object: [BrowserPanes](../BrowserPanes/BrowserPanes.md)

## Description

Method that creates a new The definition object can then be further used to construct ClientBrowserNodes that make up the tree in a custom tree-browser pane. The new ClientBrowserNodeDefinition is returned. Note that this node definition object is constructed and has an identity within the 'name space' or context of the entire owning document.

## Syntax

BrowserPanes.**CreateBrowserNodeDefinition**( ***Label*** As String, ***Id*** As Long, ***Icon*** As [ClientNodeResource](../ClientNodeResource/ClientNodeResource.md), [***ToolTipText***] As Variant, [***ExpandedIcon***] As Variant, [***DisplayState***] As Variant, [***StateIconToolTipText***] As Variant ) As [ClientBrowserNodeDefinition](../ClientBrowserNodeDefinition/ClientBrowserNodeDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Label | String | Input string that specifies the label of the browser node. This label will be displayed as the text of this resulting browser node. |
| Id | Long | Input long that uniquely identifies the Client Browser Node Definition within the scope of this Document. |
| Icon | [ClientNodeResource](../ClientNodeResource/ClientNodeResource.md) | ClientNodeResource that specifies the bitmap pictures for the node. |
| ToolTipText | Variant | Optional input string that specifies the tool tip to be displayed for the node. |
| ExpandedIcon | Variant | Optional input of a 16X16 pixel image. If this argument is not supplied then the StandardIcon is used for the purpose when the corresponding BrowserNode is to be displayed in an expanded state.   This is an optional argument whose default value is null. |
| DisplayState | Variant | Optional input BrowserNodeDisplayStateEnum that specifies the display state to use for the node.   This is an optional argument whose default value is null. |
| StateIconToolTipText | Variant | Optional input string that specifies the tool tip to be displayed for the state icon.   This is an optional argument whose default value is null. |

## Version

Introduced in version 8

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |