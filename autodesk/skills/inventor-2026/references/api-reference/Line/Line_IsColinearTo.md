# Line.IsColinearTo Property

Parent Object: [Line](../Line/Line.md)

## Description

Property that gets whether this line is colinear to the specified line, within the specified tolerance.

## Syntax

Line.**IsColinearTo**( ***Line*** As Object, [***Tolerance***] As Double ) As Boolean

## Property Value

This is a read only property whose value is a Boolean.

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Line | Object | Input object that represents a line. This object can be a linear Edge, WorkAxis, or SketchLine object. |
| Tolerance | Double | Input Double that specifies the tolerance. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Is cylindrical face interior or exterior?](../../sample-programs/Line_IsColinearTo_Sample.md) | This sample shows how to determine whether the selected cylindircal face is an exterior face or an interior (hollow) face. |

## Version

Introduced in version 9
