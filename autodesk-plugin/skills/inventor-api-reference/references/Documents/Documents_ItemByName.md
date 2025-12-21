# Documents.ItemByName Property

Parent Object: [Documents](../Documents/Documents.md)

## Description

Returns the specified Document object from the collection.

## Syntax

Documents.**ItemByName**( ***FullDocumentName*** As String ) As [Document](../Document/Document.md)

## Property Value

This is a read only property whose value is a [Document](../Document/Document.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullDocumentName | String | Input String that specifies the Document to return. If only the FullFileName is specified for part and assembly documents, the master document within the file is returned (if it exists in the collection). |

## Version

Introduced in version 10
