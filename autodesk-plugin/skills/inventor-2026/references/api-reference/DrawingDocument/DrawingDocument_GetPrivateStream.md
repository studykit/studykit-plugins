# DrawingDocument.GetPrivateStream Method

Parent Object: [DrawingDocument](../DrawingDocument/DrawingDocument.md)

## Description

Obtains a private stream within this document with the given name. Can create one, if one does not exist.

## Syntax

DrawingDocument.**GetPrivateStream**( ***StreamName*** As String, ***CreateIfNecessary*** As Boolean ) As Unknown

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StreamName | String | Input String value that specifies the name of the stream to get (31 chars max). |
| CreateIfNecessary | Boolean | Input Boolean that specifies whether to create a private stream if one does not already exist. |

## Version

Introduced in version 4
