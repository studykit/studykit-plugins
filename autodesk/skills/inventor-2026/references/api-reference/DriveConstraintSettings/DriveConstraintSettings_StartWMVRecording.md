# DriveConstraintSettings.StartWMVRecording Method

Parent Object: [DriveConstraintSettings](../DriveConstraintSettings/DriveConstraintSettings.md)

## Description

Starts recording the drive constraint animation for saving to a wmv file.

## Syntax

DriveConstraintSettings.**StartWMVRecording**( ***FullFileName*** As String, [***NetworkBandwidth***] As Long, [***ImageWidth***] As Long, [***ImageHeight***] As Long, [***AddMarkers***] As Boolean, [***MoreOptions***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input String that specifies the full file name of the wmv file to save the recording to. |
| NetworkBandwidth | Long | Optional input Long that specifies the bandwidth of your network connection in kbps. This value determines the size of the output file and the quality of recording. If not specified, this defaults to the BroadBand connection speed (250 Kbps). |
| ImageWidth | Long | Optional input Long that specifies the width of the recorded window. Defaults to 176 if not specified.   This is an optional argument whose default value is 176. |
| ImageHeight | Long | Optional input Long that specifies the height of the recorded window. Defaults to 144 if not specified.   This is an optional argument whose default value is 144. |
| AddMarkers | Boolean | Optional input Boolean that specifies whether or not to add markers to the recording. Defaults to False.   This is an optional argument whose default value is False. |
| MoreOptions | Variant | Optional input that specifies additional options. Currently unused.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2012
