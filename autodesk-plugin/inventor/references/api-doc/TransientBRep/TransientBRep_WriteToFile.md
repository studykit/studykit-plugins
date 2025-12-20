# TransientBRep.WriteToFile Method

Parent Object: [TransientBRep](../TransientBRep/TransientBRep.md)

## Description

Writes out the specified bodies as a file.

## Syntax

TransientBRep.**WriteToFile**( ***Bodies*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***FileName*** As String, [***Format***] As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Bodies | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection of Bodies that are to be written out. |
| FileName | String | Input String containing the full filename of the file to write to. |
| Format | String | Input String that defines the file format to write the body information. This can be one of the formats defined in SDK\DeveloperTools\Include\ClipboardFormats.h |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |