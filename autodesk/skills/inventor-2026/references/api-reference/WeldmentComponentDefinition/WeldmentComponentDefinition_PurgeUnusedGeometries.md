# WeldmentComponentDefinition.PurgeUnusedGeometries Method

Parent Object: [WeldmentComponentDefinition](../WeldmentComponentDefinition/WeldmentComponentDefinition.md)

## Description

Method that purges unused sketches and work features.

## Syntax

WeldmentComponentDefinition.**PurgeUnusedGeometries**( [***UnusedGeometries***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| UnusedGeometries | Variant | Optional input ObjectCollection that including the sketches and work features to purge. The unused sketches and work features can be retrieved using GetUnusedGeometries method. If this is not provided then all unused sketches and work features will be purged. |

## Version

Introduced in version 2024
