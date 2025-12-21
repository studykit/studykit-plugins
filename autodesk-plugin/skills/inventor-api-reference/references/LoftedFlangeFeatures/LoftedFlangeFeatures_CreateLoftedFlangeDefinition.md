# LoftedFlangeFeatures.CreateLoftedFlangeDefinition Method

Parent Object: [LoftedFlangeFeatures](../LoftedFlangeFeatures/LoftedFlangeFeatures.md)

## Description

Method that creates a new LoftedFlangeDefinition object.

## Remarks

This object is not a lofted flange feature but contains the information that defines a lofted flange and can be used to create a new lofted flange. The definition created defines a die formed lofted flange. To create press brake types of lofted flanges you can edit the definition before using it to create the lofted flange feature.

## Syntax

LoftedFlangeFeatures.**CreateLoftedFlangeDefinition**( ***ProfileOne*** As [Path](../Path/Path.md), ***ProfileTwo*** As [Path](../Path/Path.md) ) As [LoftedFlangeDefinition](../LoftedFlangeDefinition/LoftedFlangeDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ProfileOne | [Path](../Path/Path.md) | The first of two profiles that defines the shape of the lofted flange. Use PartFeatures.CreatePath method to create this path. |
| ProfileTwo | [Path](../Path/Path.md) | The second of two profiles that defines the shape of the lofted flange. Use PartFeatures.CreatePath method to create this path. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal lofted flange feature](../../sample-programs/LoftedFlangeFeatures_Add_Sample.md) | The following sample demonstrates the creation of a sheet metal lofted flange feature. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |