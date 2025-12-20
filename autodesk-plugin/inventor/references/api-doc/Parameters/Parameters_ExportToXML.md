# Parameters.ExportToXML Method

Parent Object: [Parameters](../Parameters/Parameters.md)

## Description

Exports parameters to XML file.

## Syntax

Parameters.**ExportToXML**( ***FileName*** As String, [***Options***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FileName | String | Input String value that specifies the XML file name. |
| Options | Variant | Optional input NameValueMap that specifies the options when export parameters to XML file. If not specified the default options will be used. Valid options are:    Name = AllParameters. Value = Boolean that specifies whether all parameters will be exported. When set to True all parameters will be exported, when set to False then only the key parameters will be exported. If not provided this defaults to True. |

## Version

Introduced in version 2026

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |