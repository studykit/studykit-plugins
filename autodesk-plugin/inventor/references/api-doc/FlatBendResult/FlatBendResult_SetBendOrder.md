# FlatBendResult.SetBendOrder Method

Parent Object: [FlatBendResult](../FlatBendResult/FlatBendResult.md)

## Description

Method that sets the bend order for this bend result. This will define a bend order override for this bend result.

## Syntax

FlatBendResult.**SetBendOrder**( ***BenderOrder*** As Long, ***AllowDuplicate*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BenderOrder | Long | Input Long that defines the order of this bend. |
| AllowDuplicate | Boolean | Input Boolean that indicates if duplicate bend order values are allowed. If True and the specified bend order value already exists on another bend result, the same bend order will be assigned to this bend result and both bend results will be defined to have an duplicate override bend order. If False and the value specified already exists then the bend values on the other bend results will modified to make room for this value. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |