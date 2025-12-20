# MarkDefinition.GetMethod Method

Parent Object: [MarkDefinition](../MarkDefinition/MarkDefinition.md)

## Description

Method that returns the mark method type info.

## Syntax

MarkDefinition.**GetMethod**( ***Method*** As [MarkMethodTypeEnum](../MarkMethodTypeEnum.md), [***pFaces***] As Variant, [***chain***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Method | [MarkMethodTypeEnum](../MarkMethodTypeEnum.md) | Output MarkMethodTypeEnum value that indicates which method is applied. |
| pFaces | Variant | Optional output the FaceCollection object. This returns the wrap to face if the method is kWrapToFaceMethodType. |
| chain | Variant | Optional output Boolean value that indicates whether the automatic face chain is applied or not. This is ignored if the method is kWrapToFaceMethodType.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |