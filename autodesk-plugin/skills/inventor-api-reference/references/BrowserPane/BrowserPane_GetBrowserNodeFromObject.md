# BrowserPane.GetBrowserNodeFromObject Method

Parent Object: [BrowserPane](../BrowserPane/BrowserPane.md)

## Description

Returns the browser node that corresponds to the input object. The method returns an error if no corresponding node is found within this pane. If multiple matches are found, the method returns the first match.

## Syntax

BrowserPane.**GetBrowserNodeFromObject**( ***NativeObject*** As Object ) As [BrowserNode](../BrowserNode/BrowserNode.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| NativeObject | Object |  |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add assembly occurrences to a new folder](../../sample-programs/BrowserPaneObject_AddBrowserFolder_Sample.md) | Demonstrates assembly occurrences to a new folder |
| [Demote occurence](../../sample-programs/BrowserPaneObject_Reorder_Demote_Sample.md) | This sample demonstrates how to demote a top level occurrence in an assembly into a new sub-assembly occurrence. |
| [Promote occurence](../../sample-programs/BrowserPaneObject_Reorder_Promote_Sample.md) | This sample demonstrates how to promote an occurrence. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |