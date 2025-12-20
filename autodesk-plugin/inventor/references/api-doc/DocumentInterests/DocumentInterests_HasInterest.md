# DocumentInterests.HasInterest Method

Parent Object: [DocumentInterests](../DocumentInterests/DocumentInterests.md)

## Description

Method that returns whether an AddIn with the input ClientId/Name has expressed interest in this document.

## Syntax

DocumentInterests.**HasInterest**( ***ClientIdOrName*** As String ) As Boolean

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ClientIdOrName | String | Input String that uniquely identifies a client. This could be the CLSID of the AddIn in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}", or the Name of the interest. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |