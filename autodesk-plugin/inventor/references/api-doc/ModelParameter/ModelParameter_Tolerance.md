# ModelParameter.Tolerance Property

Parent Object: [ModelParameter](../ModelParameter/ModelParameter.md)

## Description

Property that returns the tolerance for this parameter. This property returns Nothing in the case where the unit type of this parameter is kTextUnits or kBooleanUnits.

## Syntax

ModelParameter.**Tolerance**() As [Tolerance](../Tolerance/Tolerance.md)

## Property Value

This is a read only property whose value is a [Tolerance](../Tolerance/Tolerance.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Display information about parameter tolerances.](../../sample-programs/DumpParmeterInfo_Sample.md) | Dumps out information to the Immediate window about tolerance information associated with parameters. A part document must be active when this is run. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |