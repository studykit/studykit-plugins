# SketchBlock.ExitEdit Method

Parent Object: [SketchBlock](../SketchBlock/SketchBlock.md)

## Description

Method that causes the sketch block to return from the edit mode and into the environment specified by the input argument. If the sketch block is not currently active (i.e. this is not the same block as returned by Application.ActiveEditObject property), then this method does nothing.

## Syntax

SketchBlock.**ExitEdit**( ***ExitTo*** As [ExitTypeEnum](../ExitTypeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ExitTo | [ExitTypeEnum](../ExitTypeEnum.md) | Input ExitTypeEnum that specifies the environment to exit to. Possible values are kExitToPrevious, kExitToParent and kExitToTop. |

## Version

Introduced in version 2010
