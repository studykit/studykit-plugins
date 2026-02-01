# BalloonTips.Add Method

Parent Object: [BalloonTips](../BalloonTips/BalloonTips.md)

## Description

Method that creates a new BalloonTip object.

## Syntax

BalloonTips.**Add**( ***InternalName*** As String, ***Title*** As String, ***Message*** As String ) As [BalloonTip](../BalloonTip/BalloonTip.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InternalName | String | Input String value that specifies the internal name of the BalloonTip. This must be unique with respect to all other ballon tips. |
| Title | String | Input String value that specifies the title of the BalloonTip. |
| Message | String | Optional input String value that specifies the message for the BalloonTip. You can provide hyperlinks as part of the message using the format: <Hyperlink>http://www.yoursite.com</Hyperlink>. |

## Version

Introduced in version 2012
