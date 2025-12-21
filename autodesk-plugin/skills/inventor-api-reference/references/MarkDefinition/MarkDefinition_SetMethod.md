# MarkDefinition.SetMethod Method

Parent Object: [MarkDefinition](../MarkDefinition/MarkDefinition.md)

## Description

Method that sets the mark method type.

## Syntax

MarkDefinition.**SetMethod**( ***Method*** As [MarkMethodTypeEnum](../MarkMethodTypeEnum.md), [***Faces***] As Variant, [***chain***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Method | [MarkMethodTypeEnum](../MarkMethodTypeEnum.md) | Input MarkMethodTypeEnum value that indicates which method is applied. When any MarkGeometrySet in this definition sets Mark Through style then the valid method is kProjectionMethodType. |
| Faces | Variant | Optional input the FaceCollection object. This is required if the method is set to kWrapToFaceMethodType. |
| chain | Variant | Optional input Boolean value that specifies whether or not to perform chaining of tangent continuous faces. This is ignored if the method is not set to kWrapToFaceMethodType.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |