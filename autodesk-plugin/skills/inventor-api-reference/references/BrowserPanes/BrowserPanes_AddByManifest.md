# BrowserPanes.AddByManifest Method

Parent Object: [BrowserPanes](../BrowserPanes/BrowserPanes.md)

## Description

Method that creates and returns a new BrowserPane object. The BrowserPane created is one that is explicitly used to house un-registered ActiveX Controls.

## Syntax

BrowserPanes.**AddByManifest**( ***Name*** As String, ***InternalName*** As String, ***ManifestFileName*** As String ) As [BrowserPane](../BrowserPane/BrowserPane.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Input string that specifies the name of the browser pane. This is the name that will be displayed to the user. And thus is expected to be localized. The name must be unique with respect to the other browser panes currently created for the document. It can be changed, programmatically, at any time. It may also be used to index into the BrowserPanes collection. |
| InternalName | String | Input string that uniquely identifies the application. Suggestions are to use the 'ProgID' of the Add-In creating the pane or its CLSID in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}", although any unique string is valid. If the Add-In is going to create more than one such pane, you would want to further qualify the string by appending a suffix to the CLSID, say "{}:0" and "{}:1", etc. |
| ManifestFileName | String | Input the full filename of the manifest which defines the information of an un-registered ActiveX control. Sample manifest can be like below:  |  | | --- | | <?xml version="1.0" encoding="UTF-8" standalone="yes"?> | |

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |