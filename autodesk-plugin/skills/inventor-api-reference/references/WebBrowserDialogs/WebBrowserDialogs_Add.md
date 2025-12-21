# WebBrowserDialogs.Add Method

Parent Object: [WebBrowserDialogs](../WebBrowserDialogs/WebBrowserDialogs.md)

## Description

Method that creates a new WebBrowserDialog, the new WebBrowserDialog is returned.

## Syntax

WebBrowserDialogs.**Add**( [***InternalName***] As Variant, [***Modal***] As Boolean ) As [WebBrowserDialog](../WebBrowserDialog/WebBrowserDialog.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InternalName | Variant | Optional input String object that specifies the internal name of newly created WebBrowserDialog. If provided, the internal name should be unique in the WebBrowserDialogs collection, otherwise an error will occur. If not provided, the internal name is automatically generated. |
| Modal | Boolean | Optional input Boolean value that specifies the whether the newly created WebBrowserDialog is modal dialog or not. This defaults to False if not specified.   This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [WebBrowserDialog creation](../../sample-programs/WebBrowserDialogSample_Sample.md) | This sample demonstrates how to create a web-based browser dialog, you can use this dialog to show a html format file or navigate to a website etc.. |

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |