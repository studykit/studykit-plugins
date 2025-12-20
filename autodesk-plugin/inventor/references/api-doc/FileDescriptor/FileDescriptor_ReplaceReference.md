# FileDescriptor.ReplaceReference Method

Parent Object: [FileDescriptor](../FileDescriptor/FileDescriptor.md)

## Description

Method that replaces the referenced file.

## Remarks

The file being replaced and the replacement file must share ancestry (i.e. they must have the same InternalName). Documents have the same internal name if they are copied using 'Save Copy As' or a file explorer copy.

## Syntax

FileDescriptor.**ReplaceReference**( ***FullFileName*** As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input string that specifies the full file name to which the reference should be switched. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |