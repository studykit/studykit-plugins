# DrawingView.GetWeldmentState Method

Parent Object: [DrawingView](../DrawingView/DrawingView.md)

## Description

Method that gets the weldment option for the drawing view. The method returns a failure if the referenced model does not contain weldments.

## Syntax

DrawingView.**GetWeldmentState**( ***WeldmentState*** As [WeldmentStateEnum](../WeldmentStateEnum.md), ***Component*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| WeldmentState | [WeldmentStateEnum](../WeldmentStateEnum.md) | Output WeldmentStateEnum that returns the weldment state of the drawing view. Valid return values are kAssemblyWeldmentState, kMachiningWeldmentState, kWeldsWeldmentState and kPreparationsWeldmentState. If kPreparationsWeldmentState is returned, the Component argument returns the corresponding preparations component. |
| Component | Object | Output object that returns the component used for the Preparations weldment state. Valid return objects include an AssemblyDocument that represents the top level weldment document or a ComponentOccurrence that represents a first level occurrence in the weldment document. |

## Version

Introduced in version 2010
