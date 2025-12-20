# MassProperties.CenterOfMass Property

Parent Object: [MassProperties](../MassProperties/MassProperties.md)

## Description

Property that gets the center of mass.

## Syntax

MassProperties.**CenterOfMass**() As [Point](../Point/Point.md)

## Property Value

This is a read only property whose value is a [Point](../Point/Point.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Mass Properties from Part](../../sample-programs/MassProperties_Sample.md) | This sample demonstrates getting mass properties from a part. This sample is specific to a part document, but the MassProperties object can also be obtained from an Assembly document and from component occurrences. To run the sample you must have a part document open that contains a solid. |
| [Computing mass properties without dirtying document](../../sample-programs/MassProperties_CacheResultsOnCompute_Sample.md) | This sample demonstrates getting mass properties from a part without dirtying the document (i.e. without caching the computed results in the document). This sample is specific to a part document, but the MassProperties object can also be obtained from an Assembly document and from component occurrences. |
| [Work point at mass center](../../sample-programs/MassProperties_CenterOfMass_Sample.md) | This sample demonstrates creating a fixed work point and edit its position. It does this by computing the the center of mass of the part and creating a work point at that position. Subsequent runs of the sample reposition the work point at the new center of mass. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |