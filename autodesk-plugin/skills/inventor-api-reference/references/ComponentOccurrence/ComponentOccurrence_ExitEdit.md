# ComponentOccurrence.ExitEdit Method

Parent Object: [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md)

## Description

Method that causes the component occurrence to return from the edit mode and into the environment specified by the input argument. If the ComponentOccurrence is not currently active (i.e. this is not the same occurrence as returned by AssemblyComponentDefinition.ActiveOccurrence), then this method does nothing.

## Syntax

ComponentOccurrence.**ExitEdit**( ***ExitTo*** As [ExitTypeEnum](../ExitTypeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ExitTo | [ExitTypeEnum](../ExitTypeEnum.md) | Input ExitTypeEnum that specifies the environment to exit to. Possible values are kExitToPrevious, kExitToParent and kExitToTop. |

## Version

Introduced in version 2008
