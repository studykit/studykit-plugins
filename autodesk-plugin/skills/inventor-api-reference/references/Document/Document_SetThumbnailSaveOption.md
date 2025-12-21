# Document.SetThumbnailSaveOption Method

Parent Object: [Document](../Document/Document.md)

## Description

Method that sets the thumbnail (preview picture) save option.

## Syntax

Document.**SetThumbnailSaveOption**( ***SaveOption*** As [ThumbnailSaveOptionEnum](../ThumbnailSaveOptionEnum.md), [***ImageFullFileName***] As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SaveOption | [ThumbnailSaveOptionEnum](../ThumbnailSaveOptionEnum.md) | ThumbnailSaveOptionEnum indicating what gets saved as a thumbnail, if anything. Options include kNoThumbnail, kActiveComponentIsoViewOnSave, kActiveWindowOnSave, kActiveWindow, and kImportFromFile. |
| ImageFullFileName | String | Indicates what image file to use if SaveOption is set to kImportFromFile. |

## Version

Introduced in version 2010
