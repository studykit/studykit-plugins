# NameValueMap.Insert Method

Parent Object: [NameValueMap](../NameValueMap/NameValueMap.md)

## Description

Insert a name value pair into the name value map with specified location.

## Syntax

NameValueMap.**Insert**( ***Name*** As String, ***Value*** As Variant, [***TargetIndex***] As Variant, [***InsertBefore***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Input String that specifies the name of the key. |
| Value | Variant | Input Variant value that specifies the value of the attribute. |
| TargetIndex | Variant | Optional input an index that specifies the existing name value pair next to which the new name value pair will be inserted. This can either be a numeric value indicating the index of an existing name value pair, or it can be a string indicating the name of an existing name value pair in the NameValueMap. If this is not specified, the new name value pair will be added at the end. |
| InsertBefore | Boolean | Optional input Boolean indicating if the name value pair should be inserted before or after the target index. If not specified, a default value of True is used. This argument is ignored if the value of TargetIndex is not specified.   This is an optional argument whose default value is True. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |