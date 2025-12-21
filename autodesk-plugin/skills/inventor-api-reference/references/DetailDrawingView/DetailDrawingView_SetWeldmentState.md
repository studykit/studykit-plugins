# DetailDrawingView.SetWeldmentState Method

Parent Object: [DetailDrawingView](../DetailDrawingView/DetailDrawingView.md)

## Description

Method that sets the weldment option for the drawing view. The method returns a failure if the referenced model does not contain weldments.

## Syntax

DetailDrawingView.**SetWeldmentState**( ***WeldmentState*** As [WeldmentStateEnum](../WeldmentStateEnum.md), [***Component***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| WeldmentState | [WeldmentStateEnum](../WeldmentStateEnum.md) | Input WeldmentStateEnum that specifies the weldment state of the drawing view. Valid options are kAssemblyWeldmentState, kMachiningWeldmentState, kWeldsWeldmentState and kPreparationsWeldmentState. If kPreparationsWeldmentState is specified, the Component argument must also be specified, else the top level weldment document is assumed as the component. |
| Component | Variant | Optional input object that specifies the component to use for the Preparations weldment state. Valid input objects include an AssemblyDocument that represents the top level weldment document or a ComponentOccurrence that represents a first level occurrence in the weldment document. |

## Version

Introduced in version 2010
