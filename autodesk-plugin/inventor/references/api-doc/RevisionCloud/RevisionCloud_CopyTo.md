# RevisionCloud.CopyTo Method

Parent Object: [RevisionCloud](../RevisionCloud/RevisionCloud.md)

## Description

Method that copies the revision cloud to specified sheet.

## Syntax

RevisionCloud.**CopyTo**( ***TargetSheet*** As [Sheet](../Sheet/Sheet.md), [***NewName***] As Variant, [***Position***] As Variant ) As [RevisionCloud](../RevisionCloud/RevisionCloud.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TargetSheet | [Sheet](../Sheet/Sheet.md) | Input Sheet object that specifies the sheet to copy the revision cloud to. |
| NewName | Variant | Optional input String value that specifies the name of the new revision cloud. If not provided the default name will be used. |
| Position | Variant | Optional input Point2d object that specifies the position on the sheet to copy the revision cloud to. If not provided the default position will be used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |