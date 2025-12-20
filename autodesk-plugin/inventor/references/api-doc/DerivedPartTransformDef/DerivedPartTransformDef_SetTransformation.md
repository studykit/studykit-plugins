# DerivedPartTransformDef.SetTransformation Method

Parent Object: [DerivedPartTransformDef](../DerivedPartTransformDef/DerivedPartTransformDef.md)

## Description

Method that sets the matrix describing the transform that should be applied to the entities being derived. Operations allowed in the transform are: translation, rotation, non-uniform scale and mirror.

## Syntax

DerivedPartTransformDef.**SetTransformation**( ***Transform*** As [Matrix](../Matrix/Matrix.md), [***Mirror***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Transform | [Matrix](../Matrix/Matrix.md) | Input object that specifies the transform for the derived part. |
| Mirror | Boolean | Optional input Boolean that specifies whether the derived part should be mirrored. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |