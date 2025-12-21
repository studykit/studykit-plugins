# SurfaceBody.SetAppearanceTextureMappingData Method

Parent Object: [SurfaceBody](../SurfaceBody/SurfaceBody.md)

## Description

Method that sets the texture mapping type and alignment. Setting this value is only valid when the appearance assigned to the body has a texture defined.

## Syntax

SurfaceBody.**SetAppearanceTextureMappingData**( ***TextureMappingType*** As [TextureMappingTypeEnum](../TextureMappingTypeEnum.md), [***TextureMappingAlignment***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TextureMappingType | [TextureMappingTypeEnum](../TextureMappingTypeEnum.md) | Input texture mapping type applies to the object. |
| TextureMappingAlignment | Variant | Optional input unit vector that indicates the texture mapping alignment. This argument will be ignored if the TextureMappingType is not kCylindricalMappingType or kSphericalMappingType. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |