# UnfoldMethod.DeleteEquation Method

Parent Object: [UnfoldMethod](../UnfoldMethod/UnfoldMethod.md)

## Description

Method that deletes the specified equation. An equation unfold method always needs to have at least one equation. Deleting the last equation will cause a default equation to be created.

## Syntax

UnfoldMethod.**DeleteEquation**( ***Index*** As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Long that specifies which equation to delete. Valid values are 1 to the current value of the UnfoldMethod.EquationCount property. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |