# MassProperties.AvailableAccuracy Property

Parent Object: [MassProperties](../MassProperties/MassProperties.md)

## Description

Indicates the computational accuracy of mass properties calculations.

## Syntax

MassProperties.**AvailableAccuracy**() As [MassPropertiesAccuracyEnum](../MassPropertiesAccuracyEnum.md)

## Property Value

This is a read only property whose value is a [MassPropertiesAccuracyEnum](../MassPropertiesAccuracyEnum.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Computing mass properties without dirtying document](../../sample-programs/MassProperties_CacheResultsOnCompute_Sample.md) | This sample demonstrates getting mass properties from a part without dirtying the document (i.e. without caching the computed results in the document). This sample is specific to a part document, but the MassProperties object can also be obtained from an Assembly document and from component occurrences. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |