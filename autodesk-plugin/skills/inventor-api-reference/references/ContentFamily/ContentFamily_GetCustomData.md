# ContentFamily.GetCustomData Method

Parent Object: [ContentFamily](../ContentFamily/ContentFamily.md)

## Description

Method that gets the specified custom data from the family. The custom data is returned if it exists or this method will fail if the specified custom data does not exist. You can use the HasCustomData property to determine if custom data exists.

## Syntax

ContentFamily.**GetCustomData**( ***ClientId*** As String, ***InternalName*** As String, ***CustomData***() As Byte )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ClientId | String | Input String that uniquely identifies the application that created the custom data. This is commonly the CLSID of the Add-In in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}", but it can be any string. |
| InternalName | String | Input String value that specifies the unique name of the custom data to retrieve. |
| CustomData | Byte | Output array of bytes containing the custom data. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |