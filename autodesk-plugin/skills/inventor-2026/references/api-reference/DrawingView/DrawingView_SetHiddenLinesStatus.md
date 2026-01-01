# DrawingView.SetHiddenLinesStatus Method

Parent Object: [DrawingView](../DrawingView/DrawingView.md)

## Description

Method that sets the hidden lines status of a component in the drawing view.

## Syntax

DrawingView.**SetHiddenLinesStatus**( ***Component*** As Object, ***visibleStatus*** As [HiddenLinesStatusEnum](../HiddenLinesStatusEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Component | Object | Input Document, ComponentOccurrence, ComponentOccurrenceProxy, SurfaceBody, SurfaceBodyProxy, MeshFeature or MeshFeatureProxy object to indicate a component in the drawing view. |
| visibleStatus | [HiddenLinesStatusEnum](../HiddenLinesStatusEnum.md) | Input HiddenLinesStatusEnum value to specify the hidden line status for the component. Valid values are kAllHiddenLinesVisible and kAllHiddenLinesInvisible. |

## Version

Introduced in version 2022
