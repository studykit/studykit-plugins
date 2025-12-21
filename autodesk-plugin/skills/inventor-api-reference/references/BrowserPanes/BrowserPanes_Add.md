# BrowserPanes.Add Method

Parent Object: [BrowserPanes](../BrowserPanes/BrowserPanes.md)

## Description

Method that creates and returns a new BrowserPane object. The BrowserPane created is one that is explicitly used to house ActiveX controls.

## Syntax

BrowserPanes.**Add**( ***Name*** As String, ***InternalName*** As String ) As [BrowserPane](../BrowserPane/BrowserPane.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Input String that specifies the name of the BrowserPane object. This is the name that will be displayed to the user. The name must be unique with respect to the other browser panes currently created for the document. It can be changed programmatically at any time, and can be localized. It can also be used as an index into the BrowserPanes collection. |
| InternalName | String | Input string that identifies the ActiveX control that will be displayed on the pane. This identifier can be either the ProgID or the GUID of the control as a string, (including the braces "{ }"). This string will also be used to uniquely identify the BrowserPane within the collection. This identifier string once provided cannot be changed. |

## Version

Introduced in version 5
