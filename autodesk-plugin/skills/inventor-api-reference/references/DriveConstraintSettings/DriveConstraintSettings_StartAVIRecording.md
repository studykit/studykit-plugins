# DriveConstraintSettings.StartAVIRecording Method

Parent Object: [DriveConstraintSettings](../DriveConstraintSettings/DriveConstraintSettings.md)

## Description

Starts recording the drive constraint animation for saving to an avi file.

## Syntax

DriveConstraintSettings.**StartAVIRecording**( ***FullFileName*** As String, [***Compressor***] As String, [***CompressionQuality***] As Long, [***MoreOptions***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input String that specifies the full file name of the avi file to save the recording to. |
| Compressor | String | Optional input String that specifies the name of the compressor to use. The string should be a FourCC code (see http://ww.fourcc.org for details). If not specified, the default is used. |
| CompressionQuality | Long | Optional input Long that specifies the compression quality. The valid range of values is 0 to 100. If not specified, a default value of 75 is used.   This is an optional argument whose default value is 75. |
| MoreOptions | Variant | Optional input that specifies additional options. Currently unused.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |