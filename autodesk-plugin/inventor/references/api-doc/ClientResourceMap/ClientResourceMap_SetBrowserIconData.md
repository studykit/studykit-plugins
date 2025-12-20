# ClientResourceMap.SetBrowserIconData Method

Parent Object: [ClientResourceMap](../ClientResourceMap/ClientResourceMap.md)

## Description

Represents a ClientResourceMaps collection Object.

## Syntax

ClientResourceMap.**SetBrowserIconData**( ***IconData*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***Theme*** As String, [***AsDefault***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| IconData | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap that specifies the icon data. The data includes a batch of icon info as below: Name = A unique string in this NameValueMap to indicate the name of an icon. This name is also used for browser node definition to specify a client icon. Value = IPictureDisp object that indicate an icon of 16 pixels wide and 16 pixels high. |
| Theme | String | Input String value that indicates a Theme name. |
| AsDefault | Variant | Optional input Boolean value that specifies whether this icon data will be used as default icons for other Theme if no icon data is set for that Theme. |

## Version

Introduced in version 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |