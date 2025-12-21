# LoftFeatures.Add Method

Parent Object: [LoftFeatures](../LoftFeatures/LoftFeatures.md)

## Description

Method that creates a new loft.

## Syntax

LoftFeatures.**Add**( ***Definition*** As [LoftDefinition](../LoftDefinition/LoftDefinition.md) ) As [LoftFeature](../LoftFeature/LoftFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Definition | [LoftDefinition](../LoftDefinition/LoftDefinition.md) | Input LoftDefinition object that defines the input definition for the loft. The LoftDefinition object can be created using the CreateLoftDefinition method of the LoftFeatures object. The LoftDefinition object defines the following input data for creating the loft feature: the loft sections, the boundary conditions for the starting and ending sections, a centerline or rails with any applicable boundary conditions, the mapping between the sections, an option to indicate whether the loft should be closed or not and an option to indicate whether tangent faces should be merged or not. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Loft Feature With Non-Planar Section](../../sample-programs/LoftFeature_Sample.md) | This sample demonstrates the creation of a loft feature. It uses two sections for the loft, one is from a 2d sketch and the other is a non-planar section from a 3d sketch. Because one of the sketches isn't planar, a surface is created instead of a solid. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |