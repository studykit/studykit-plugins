# EdgeSymbol.CopyTo Method

Parent Object: [EdgeSymbol](../EdgeSymbol/EdgeSymbol.md)

## Description

Method that copies the edge symbol to specified sheet.

## Syntax

EdgeSymbol.**CopyTo**( ***TargetSheet*** As [Sheet](../Sheet/Sheet.md), [***NewName***] As Variant, [***Position***] As Variant ) As [EdgeSymbol](../EdgeSymbol/EdgeSymbol.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TargetSheet | [Sheet](../Sheet/Sheet.md) | Input Sheet object that specifies the sheet to copy the edge symbol to. |
| NewName | Variant | Optional input String value that specifies the name of the new edge symbol. If not provided the default name will be used. |
| Position | Variant | Optional input Point2d object that specifies the position on the sheet to copy the edge symbol to. If not provided the default position will be used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |