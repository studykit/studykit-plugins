# GeometryIntent.IntentType Property

Parent Object: [GeometryIntent](../GeometryIntent/GeometryIntent.md)

## Description

Property that returns intent type indicating the type of value that the Intent property will return. Possible return values are kPointEnumIntent (a PointIntentEnum will be returned), kPoint2dIntent (a Point2d object will be returned), kParameterIntent (a double value will be returned), kGeometryIntent (a DrawingCurve or a SketchEntity will be returned) or kNoPointIntent (the GeometryIntent is not a point and the Intent property will not return a meaningful value).

## Syntax

GeometryIntent.**IntentType**() As [IntentTypeEnum](../IntentTypeEnum.md)

## Property Value

This is a read only property whose value is an [IntentTypeEnum](../IntentTypeEnum.md).

## Version

Introduced in version 11
