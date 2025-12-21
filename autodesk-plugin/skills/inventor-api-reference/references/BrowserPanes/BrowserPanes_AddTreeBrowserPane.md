# BrowserPanes.AddTreeBrowserPane Method

Parent Object: [BrowserPanes](../BrowserPanes/BrowserPanes.md)

## Description

Method that creates and returns a new BrowserPane object. The BrowserPane created is one in which Inventor's BrowserTreeNodes can be instanced to generate a completely customizable tree view.

## Syntax

BrowserPanes.**AddTreeBrowserPane**( ***Name*** As String, ***InternalName*** As String, ***TopNodeDefinition*** As [BrowserNodeDefinition](../BrowserNodeDefinition/BrowserNodeDefinition.md) ) As [BrowserPane](../BrowserPane/BrowserPane.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Input string that specifies the name of the browser pane. This is the name that will be displayed to the user. The name must be unique with respect to the other browser panes currently created for the document. It can be changed programmatically at any time, and can be localized. It can also be used as an index into the BrowserPanes collection. |
| InternalName | String | Input string that uniquely identifies the application. Suggestions are to use the 'ProgID' of the Add-In creating the pane or its CLSID in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}", although any unique string is valid. If the Add-In is going to create more than one such pane, you would want to further qualify the string by appending a suffix to the CLSID, say "{}:0" and "{}:1", etc. |
| TopNodeDefinition | [BrowserNodeDefinition](../BrowserNodeDefinition/BrowserNodeDefinition.md) | Input definition object that will be used to build the single topmost node that starts the browser tree. |

## Version

Introduced in version 8

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |