# SurfaceBodyProxy.GetAppearanceTextureMappingData Method

Parent Object: [SurfaceBodyProxy](../SurfaceBodyProxy/SurfaceBodyProxy.md)

## Description

Gets the texture mapping type and alignment.

## Syntax

SurfaceBodyProxy.**GetAppearanceTextureMappingData**( ***TextureMappingType*** As [TextureMappingTypeEnum](../TextureMappingTypeEnum.md), [***TextureMappingAlignment***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TextureMappingType | [TextureMappingTypeEnum](../TextureMappingTypeEnum.md) | Output texture mapping type applied to the object. |
| TextureMappingAlignment | Variant | Output unit vector that indicates the texture mapping alignment. This value will be invalid if the TextureMappingType is not kCylindricalMappingType or kSphericalMappingType. |

## Version

Introduced in version 2014
