# OriginIndicator.Delete Method

Parent Object: [OriginIndicator](../OriginIndicator/OriginIndicator.md)

## Description

Method that deletes this origin indicator. This fails if this origin indicator is referenced by ordinate dimensions or hole tables.

## Syntax

OriginIndicator.**Delete**( [***ForceToDelete***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ForceToDelete | Variant | Optional input Boolean value that specifies whether to force to delete the origin indicator or not. If set this to False and the OriginIndicator.InUse returns True then the delete will fail. If set this to True and the OriginIndicator.InUse returns True then the delete will also delete the referencing dimensions and tables. |

## Version

Introduced in version 2024.1

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |