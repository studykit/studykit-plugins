# DesignProject.SetCustomSection Method

Parent Object: [DesignProject](../DesignProject/DesignProject.md)

## Description

Method that adds or modifies a custom section (in the form of an XML string) in the project file. If a section with the given name is found, the section is replaced, else the section is added.

## Syntax

DesignProject.**SetCustomSection**( ***Name*** As String, ***CustomSection*** As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Input String that specifies name of the custom section in the project file. The name should be as unique and human-readable as possible. If a section with this name is found, the existing section is replaced with the input CustomSection string. If not found, a new section is created. |
| CustomSection | String | Input String containing an XML string with custom data to be stored in the project file. The name of the section should be included in this XML string, for example 'ApplicationXYZProjectOptions'. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |