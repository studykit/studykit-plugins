# DrawingPrintManager.GetSheetRange Method

Parent Object: [DrawingPrintManager](../DrawingPrintManager/DrawingPrintManager.md)

## Description

Method that gets the sheet range to print. The sheet range is only used when the PrintRange property is set to kPrintSheetRange.

## Syntax

DrawingPrintManager.**GetSheetRange**( ***FromSheet*** As Long, ***ToSheet*** As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FromSheet | Long | Output Long value that specifies the first sheet of the range to print. |
| ToSheet | Long | Output Long value that specifies the last sheet of the range to print. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Printing - Drawing Print](../../sample-programs/DrawingPrintManager_SetSheetRange_Sample.md) | This sample demonstrates how to print a drawing, setting specifics such as sheet range. |

## Version

Introduced in version 5
