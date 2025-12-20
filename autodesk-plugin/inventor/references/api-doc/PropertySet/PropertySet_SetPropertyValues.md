# PropertySet.SetPropertyValues Method

Parent Object: [PropertySet](../PropertySet/PropertySet.md)

## Description

Method that batch sets property values in the PropertySet. If a specified name is not existent in the property set a new property with the specified name will be created.

## Syntax

PropertySet.**SetPropertyValues**( ***PropertyNames***() As String, ***PropertyValues***() As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PropertyNames | String | Input String array that indicates the property names. |
| PropertyValues | Variant | Input Variant array that indicates the property values. The sequence of the values are the same as the corresponding PropNames. |

## Version

Introduced in version 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |