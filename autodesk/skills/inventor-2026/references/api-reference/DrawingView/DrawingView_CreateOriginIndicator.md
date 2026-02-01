# DrawingView.CreateOriginIndicator Method

Parent Object: [DrawingView](../DrawingView/DrawingView.md)

## Description

Method that creates the origin indicator for ordinate dimensions and hole tables. The specified input GeometryIntent object must be associated with this drawing view, otherwise this method will fail.

## Remarks

This method will create the origin indicator on the view if one does not already exist as indicated by the HasOriginIndicator property returning a value of False. If an origin indicator has already been created for the view as indicated by the HasOriginIndicator property returning a value of True, this method will fail. The OriginIndicator property will return this already existing origin indicator. If the origin point with which this origin indicator is associated needs to be changed, it can be done using the OriginIndicator.Intent property.

## Syntax

DrawingView.**CreateOriginIndicator**( ***Intent*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Intent | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input GeometryIntent object that specifies the origin point with which the origin indicator is associated. The GeometryIntent object can be created using the Sheet.CreateGeometryIntent method. Valid intent values are points. If an invalid intent value is specified, this method will fail. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creating hole tables](../../sample-programs/HoleTables_Add_Sample.md) | This sample demonstrates the creation of hole tables in a drawing. |
| [Create ordinate dimension](../../sample-programs/OrdinateDimensions_Add_Sample.md) | This sample demonstrates the creation of ordinate dimensions in a drawing document. |

## Version

Introduced in version 2009
