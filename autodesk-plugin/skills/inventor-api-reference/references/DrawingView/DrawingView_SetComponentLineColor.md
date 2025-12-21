# DrawingView.SetComponentLineColor Method

Parent Object: [DrawingView](../DrawingView/DrawingView.md)

## Description

Method that sets color for a component in the drawing view.

## Syntax

DrawingView.**SetComponentLineColor**( ***Component*** As Object, ***Color*** As [Color](../Color/Color.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Component | Object | Input Document, ComponentOccurrence, ComponentOccurrenceProxy, SurfaceBody, SurfaceBodyProxy, PartFeature or PartFeatureProxy object to indicate a component in the drawing view. |
| Color | [Color](../Color/Color.md) | Input Color object to set the color for the component in the drawing view. This the color has its ColorSourceType set to kLayerColorSource or kAutomaticColorSource then the color of the component will be set by layer or automatic. |

## Version

Introduced in version 2025.1

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |