# BrowserPane.AddBrowserFolder Method

Parent Object: [BrowserPane](../BrowserPane/BrowserPane.md)

## Description

Creates a new browser folder at the location specified by the input nodes.

## Syntax

BrowserPane.**AddBrowserFolder**( [***Name***] As String, [***BrowserNodes***] As Variant ) As [BrowserFolder](../BrowserFolder/BrowserFolder.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Optional input String that specifies a name for the folder. If not specified, the default naming scheme is used to assign a name to the folder. |
| BrowserNodes | Variant | Optional input ObjectCollection containing BrowserNode objects to create the folder for. If not specified, an empty folder is created as the last node in the browser. The input nodes should be contiguous in the browser. If not contiguous, Inventor attempts to reorder the nodes so they are contiguous before putting them in a folder. Use GetBrowserNodeFromObject method to get corresponding browser nodes for Inventor objects.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add assembly occurrences to a new folder](../../sample-programs/BrowserPaneObject_AddBrowserFolder_Sample.md) | Demonstrates assembly occurrences to a new folder |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |