# ContentFamily.HasCustomData Method

Parent Object: [ContentFamily](../ContentFamily/ContentFamily.md)

## Description

Property indicates if the family has the specified custom data. Returns True if the data exists.

## Syntax

ContentFamily.**HasCustomData**( ***ClientId*** As String, ***InternalName*** As String ) As Boolean

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ClientId | String | Input String that uniquely identifies the application that created the custom data. This is commonly the CLSID of the Add-In in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}", but can be any string. |
| InternalName | String | Input String value that specifies the unique name of the custom data. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |