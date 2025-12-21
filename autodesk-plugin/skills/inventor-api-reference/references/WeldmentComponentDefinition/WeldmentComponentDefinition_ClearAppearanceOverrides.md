# WeldmentComponentDefinition.ClearAppearanceOverrides Method

Parent Object: [WeldmentComponentDefinition](../WeldmentComponentDefinition/WeldmentComponentDefinition.md)

## Description

Clears the appearance overrides on the provided objects. The objects can include faces, features, work surfaces, surface bodies and occurrences.

## Syntax

WeldmentComponentDefinition.**ClearAppearanceOverrides**( [***AppearanceOverrideObjects***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AppearanceOverrideObjects | Variant | Optional input ObjectCollection including occurrences to clear their appearance overrides. If this argument is not provided, then it will clear all the appearance overrides in active design view. If an object is provided that does not have an override, it is ignored. |

## Version

Introduced in version 2014
