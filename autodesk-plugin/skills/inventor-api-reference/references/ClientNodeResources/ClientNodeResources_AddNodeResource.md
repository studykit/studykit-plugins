# ClientNodeResources.AddNodeResource Method

Parent Object: [ClientNodeResources](../ClientNodeResources/ClientNodeResources.md)

## Description

Method which creates new client resource object.

## Syntax

ClientNodeResources.**AddNodeResource**( ***ClientId*** As String, ***Id*** As Long, ***IconName*** As String ) As [ClientNodeResource](../ClientNodeResource/ClientNodeResource.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ClientId | String | Input string that uniquely identifies the client. Suggestions are the ‘ProgID’ of the Add-In creating the resource or the its CLSID in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}", although any unique string is valid. |
| Id | Long | Input integer identifier that uniquely identifies the resource to the client. This identifier better be unique within the context of this owning document, and within this AddIn. The ClientId and the Id taken together uniquely identify this object. |
| IconName | String | Input String value that specifies name of a client icon from ClientResourceMap. If use default node icon an empty string can be provided. |

## Version

Introduced in version 2022
