# DetailDrawingView.CreateOriginIndicator Method

Parent Object: [DetailDrawingView](../DetailDrawingView/DetailDrawingView.md)

## Description

Method that creates the origin indicator for ordinate dimensions and hole tables. The specified input GeometryIntent object must be associated with this drawing view, otherwise this method will fail.

## Syntax

DetailDrawingView.**CreateOriginIndicator**( ***Intent*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Intent | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input GeometryIntent object that specifies the origin point with which the origin indicator is associated. The GeometryIntent object can be created using the Sheet.CreateGeometryIntent method. Valid intent values are points. If an invalid intent value is specified, this method will fail. |

## Version

Introduced in version 2009
