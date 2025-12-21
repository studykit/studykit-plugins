# ClientResourceMaps.Add Method

Parent Object: [ClientResourceMaps](../ClientResourceMaps/ClientResourceMaps.md)

## Description

Adds a ClientResourceMap object.

## Syntax

ClientResourceMaps.**Add**( ***ClientId*** As String, ***Id*** As Long ) As [ClientResourceMap](../ClientResourceMap/ClientResourceMap.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ClientId | String | Input string that uniquely identifies the client. Some suggestions might be the 'ProgID' of the Add-In creating the resource, or its CLSID in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}", although any unique string is valid. |
| Id | Long | Input Long value that uniquely identifies the ClientResourceMap. This identifier must be unique within the context of this owning document, and within this AddIn. The ClientId and the Id taken together uniquely identify this object. |

## Version

Introduced in version 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |