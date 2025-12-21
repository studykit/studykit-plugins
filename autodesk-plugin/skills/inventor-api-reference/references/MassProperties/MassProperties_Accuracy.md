# MassProperties.Accuracy Property

Parent Object: [MassProperties](../MassProperties/MassProperties.md)

## Description

Read-write property that gets/sets the desired level of computational accuracy of the mass property calculations.

## Syntax

MassProperties.**Accuracy**() As [MassPropertiesAccuracyEnum](../MassPropertiesAccuracyEnum.md)

## Property Value

This is a read/write property whose value is a [MassPropertiesAccuracyEnum](../MassPropertiesAccuracyEnum.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Mass Properties from Part](../../sample-programs/MassProperties_Sample.md) | This sample demonstrates getting mass properties from a part. This sample is specific to a part document, but the MassProperties object can also be obtained from an Assembly document and from component occurrences. To run the sample you must have a part document open that contains a solid. |
| [Computing mass properties without dirtying document](../../sample-programs/MassProperties_CacheResultsOnCompute_Sample.md) | This sample demonstrates getting mass properties from a part without dirtying the document (i.e. without caching the computed results in the document). This sample is specific to a part document, but the MassProperties object can also be obtained from an Assembly document and from component occurrences. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |