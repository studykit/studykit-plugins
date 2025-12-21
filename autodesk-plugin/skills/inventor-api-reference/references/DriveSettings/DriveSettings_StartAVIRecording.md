# DriveSettings.StartAVIRecording Method

Parent Object: [DriveSettings](../DriveSettings/DriveSettings.md)

## Description

Method that starts recording the drive relationship animation for saving to an avi file. Use the StopRecording method to stop recording and generate the animation file.

## Syntax

DriveSettings.**StartAVIRecording**( ***FullFileName*** As String, [***Compressor***] As String, [***CompressionQuality***] As Long, [***MoreOptions***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input String that specifies the full file name of the avi file to save the recording to. |
| Compressor | String | Optional input String that specifies the name of the compressor to use. The string should be a FourCC code ( see http://www.fourcc.org/ for details). If not specified, the default is used. |
| CompressionQuality | Long | Optional input Long that specifies the compression quality. The valid range of values is 0 to 100. If not specified, a default value of 75 is used.   This is an optional argument whose default value is 75. |
| MoreOptions | Variant | Optional input that specifies additional options. This argument is currently not used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2014
