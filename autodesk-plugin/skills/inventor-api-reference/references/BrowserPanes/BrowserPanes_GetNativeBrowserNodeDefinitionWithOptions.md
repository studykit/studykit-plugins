# BrowserPanes.GetNativeBrowserNodeDefinitionWithOptions Method

Parent Object: [BrowserPanes](../BrowserPanes/BrowserPanes.md)

## Description

Method that returns the NativeBrowserNodeDefinition that corresponds to the input object.

## Syntax

BrowserPanes.**GetNativeBrowserNodeDefinitionWithOptions**( ***NativeObject*** As Object, [***Options***] As Variant ) As [NativeBrowserNodeDefinition](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| NativeObject | Object | Input object to return the definition for. |
| Options | Variant | Optinoal input NameValueMap object to specify options for how to find the definition. Below are the valid values: Name = DepthFirst, Value = Boolean that indicates whether the search is depth first. If this is set to Ture then it will search the browser nodes recursively in depth level, otherwise it will search the top browser nodes first and then their children. If this is not specified it defaults to True. |

## Version

Introduced in version 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |